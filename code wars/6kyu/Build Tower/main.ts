export const towerBuilder = (nFloors: number): string[] => {
    const arr: Array<string> = []
    for (let i = 0; i < nFloors; i++) {
        const spaces = " ".repeat(nFloors - i - 1);
        const stars = "*".repeat(2 * i + 1);
        arr.push(spaces + stars + spaces);
    }
    return arr
}
// Could be golfed this way:
export const towerBuilderTwo = (nFloors: number): string[] => {
    return Array.from({length: nFloors}, (_, i) => `${" ".repeat(nFloors - i - 1)}${"*".repeat(2 * i + 1)}${" ".repeat(nFloors - i - 1)}`)
   }