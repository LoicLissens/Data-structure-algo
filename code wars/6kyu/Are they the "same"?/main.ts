export function comp(a1: number[] | null, a2: number[] | null): boolean {
    if (a1 === null || a2 === null) return false;
    if (a1.length !== a2.length) return false;
    const a3 = a1.map((x) => x * x).sort((a, b) => a - b);
    a2.sort((a, b) => a - b);
    return a3.every((x, i) => x === a2[i]);
  }