interface IStack<T> {
    push(item: T): void;
    pop(): T | undefined;
    peek(): T | undefined
  }
class Stack<T> implements IStack<T> {
    _count: number
    storage: { [key: number]: T }
    constructor() {
        this._count = 0
        this.storage = {}
    }
    pop(): T | undefined{
        if (this._count === 0)  return undefined
        this._count--
        const res =  this.storage[this._count]
        delete this.storage[this._count]
        return res
    }
    push(el:T): void{
        this.storage[this._count] = el
        this._count++
    }
    get length(): number{
        return this._count
    }
    peek(): T | undefined{
        if (this._count ===0) return undefined
        return this.storage[this._count -1]
    }
}

function main(){
    const pal = "racecar"
    let newStr = ""
    const stack = new Stack<string>()
    for (const char of pal){
        stack.push(char)
    }
    console.log(stack.length); //7
    console.log(stack.peek()); // r
    for (let i = 0; i < pal.length;i++){
        newStr += stack.pop()
    }
    console.log(pal == newStr);
}
main()