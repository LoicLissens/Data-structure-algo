const compute = (a:number,b:number,op:string): number =>{
    if (op === "+") return a+b;
    if (op === "-") return a-b;
    if (op === "*") return a*b;
    if (op === "/") return a/b;
    throw new Error("Invalid operator")
  }
  export function calc(expr: string): number {
    const stack:Array<number> = []
    if (expr.length === 0) return 0;
    const validOp =   ["+","-","*","/"]
    for (let char of expr.split(" ")){
      if (!validOp.includes(char)){
        stack.push(parseFloat(char))
      }else{
        const b = stack.pop() as number
        const a =  stack.pop() as number
        const res =  compute(a,b,char)
        console.log({
          a,b,res
        })
        stack.push(res)
      }
    }
    return stack[0]
  }
  // Can be golfed:
  export function calc(expr: string): number {
    const stack: number[] = [];
    const reduce = (op: (a: number, b: number) => number) => stack.push(op(stack.pop()!, stack.pop()!));
    for (const x of expr.split(' ')) {
      switch (x) {
          case '+': reduce((a, b) => a + b); break;
          case '-': reduce((a, b) => b - a); break;
          case '*': reduce((a, b) => a * b); break;
          case '/': reduce((a, b) => b / a); break;
          default: stack.push(+x); break;
      }
    }
    return stack[0];
  }