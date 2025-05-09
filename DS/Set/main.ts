interface ISet<T> {
    has(item: T): boolean;
    add(item: T): boolean;
    remove(item: T): boolean;
    union(set: ISet<T>): ISet<T>;
    intersection(set: ISet<T>): ISet<T>;
    subset(set: ISet<T>): boolean;
    difference(set: ISet<T>): ISet<T>
}
// Not optimised for perfs
class CustomSet<T> implements ISet<T> {
    private _collection: Array<T>
    constructor() {
        this._collection = []
    }
    get values(): Array<T> {
        return this._collection
    }
    get size(): number {
        return this._collection.length
    }
    has(item: T): boolean {
        return this._collection.indexOf(item) != -1
    }
    add(item: T): boolean {
        if (this.has(item)) return false;
        this._collection.push(item)
        return true
    }
    remove(item: T): boolean {
        if (!this.has(item)) return false;
        const i = this._collection.indexOf(item)
        this._collection.splice(i, 1)
        return true
    }
    union(secondeSet: CustomSet<T>): CustomSet<T> {
        let newSet = new CustomSet<T>()
        const first = this.values
        const sec = secondeSet.values
        first.forEach(e => newSet.add(e))
        sec.forEach(e => newSet.add(e))
        return newSet
    }
    intersection(set: CustomSet<T>): CustomSet<T> {
        let newSet = new CustomSet<T>()
        set.values.forEach((e) => {
            if (this.has(e)) newSet.add(e);
        })
        return newSet
    }
    subset(set: CustomSet<T>): boolean {
        const primary = this.values
        return primary.every((e) => set.has(e))
    }
    difference(set: CustomSet<T>): CustomSet<T> {
        const diff = new CustomSet<T>()
        this.values.forEach((e) => {
            if (!set.has(e)) diff.add(e);
        })
        set.values.forEach((e) => {
            if (!this.has(e)) diff.add(e);
        })
        return diff
    }
}
// Opti for perf
// Main improvment comes from the use of a map (bettwer for lookup add and remove, we don't have to use indexOf which is costly)
// Map (over object) can have any type as key, has .size builtin prop, order is preserved, for intensive add/rem it's more opti
// to f
class PerfCustomSet<T> implements ISet<T> {
    private _map: Map<string, T>;
    private _toKey: (item: T) => string;

    constructor(toKey: (item: T) => string = JSON.stringify) {
        this._map = new Map<string, T>();
        this._toKey = toKey;
    }

    get values(): Array<T> {
        return Array.from(this._map.values());
    }

    get size(): number {
        return this._map.size;
    }

    has(item: T): boolean {
        return this._map.has(this._toKey(item));
    }

    add(item: T): boolean {
        const key = this._toKey(item);
        if (this._map.has(key)) return false;
        this._map.set(key, item);
        return true;
    }

    remove(item: T): boolean {
        const key = this._toKey(item);
        if (!this._map.has(key)) return false;
        this._map.delete(key);
        return true;
    }

    union(secondSet: PerfCustomSet<T>): PerfCustomSet<T> {
        const newSet = new PerfCustomSet<T>(this._toKey);

        this.forEach(item => newSet.add(item));
        secondSet.values.forEach(item => newSet.add(item));

        return newSet;
    }

    intersection(set: PerfCustomSet<T>): PerfCustomSet<T> {
        const newSet = new PerfCustomSet<T>(this._toKey);

        // Only add items that exist in both sets
        this.values.forEach(item => {
            if (set.has(item)) newSet.add(item);
        });

        return newSet;
    }

    subset(set: PerfCustomSet<T>): boolean {
        return this.values.every(item => set.has(item));
    }

    difference(set: PerfCustomSet<T>): PerfCustomSet<T> {
        const newSet = new PerfCustomSet<T>(this._toKey);
        this.values.forEach(item => {
            if (!set.has(item)) newSet.add(item);
        });
        return newSet;
    }

    symmetricDifference(set: PerfCustomSet<T>): PerfCustomSet<T> {
        const newSet = new PerfCustomSet<T>(this._toKey);

        this.forEach(item => {
            if (!set.has(item)) newSet.add(item);
        });
        set.forEach(item => {
            if (!this.has(item)) newSet.add(item);
        });
        return newSet;
    }

    forEach(callback: (item: T) => void): void {
        this._map.forEach((value) => callback(value));
    }

    static fromArray<T>(array: T[], toKey: (item: T) => string = JSON.stringify): PerfCustomSet<T> {
        const set = new PerfCustomSet<T>();
        array.forEach(item => set.add(item));
        return set;
    }
}

function main() {
    // const setOne = new CustomSet<number>()
    // const setTwo = new CustomSet<number>()
    // console.log(setOne.add(1)); // true
    // console.log(setOne.add(1)); false
    // console.log(setOne.has(1)); // true
    // setTwo.add(1)
    // setTwo.add(2)
    // setTwo.add(3)
    // const setThree = setOne.intersection(setTwo)
    // console.log(setThree.size); // 1
    // console.log(setThree.values); // [1]
    // const setFour = setOne.union(setTwo)
    // console.log(setFour.size); //3
    // console.log(setFour.values); // [1,2,3]
    // console.log(setOne.subset(setFour)); // true
    // setOne.add(5) // now [1,5]
    // console.log(setFour.difference(setOne).values);

    const setOne = new PerfCustomSet<number>()
    const setTwo = new PerfCustomSet<number>()
    console.log(setOne.add(1)); // true
    console.log(setOne.add(1)); false
    console.log(setOne.has(1)); // true
    setTwo.add(1)
    setTwo.add(2)
    setTwo.add(3)
    const setThree = setOne.intersection(setTwo)
    console.log(setThree.size); // 1
    console.log(setThree.values); // [1]
    const setFour = setOne.union(setTwo)
    console.log(setFour.size); //3G
    console.log(setFour.values); // [1,2,3]
    console.log(setOne.subset(setFour)); // true
    setOne.add(5) // now [1,5]
    console.log(setFour.difference(setOne).values);
}
main()