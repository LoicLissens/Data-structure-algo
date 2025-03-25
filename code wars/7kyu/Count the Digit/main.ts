export class G964 {
    public static nbDig(n: number, d: number): number {
        let count = 0
        const arr: Array<number> = [...Array(n+1).keys()]
        arr.forEach(e => {
          const num:string = e**2 + ''
          count += num.split('').filter(e => e === d.toString()).length
        })
        return count
    }
}
// or
export class G964 {
    public static nbDig(n: number, d: number): number {
        let count: number = 0;
        for (let k: number = 0; k <= n; k++) {
            count += (k * k).toString().split(d.toString()).length - 1;
        }
        return count;
    }
}