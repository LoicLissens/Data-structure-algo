function newAvg(arr: number[], newavg: number): number {
    let res: number = (newavg * (arr.length + 1)) - arr.reduce((a, b) => a + b, 0)
    if (res <= 0) throw "Expected New Average is too low"
    return Math.ceil(res)
  }