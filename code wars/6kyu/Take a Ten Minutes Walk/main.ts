function isValidWalk(walk:string[]) {
    const length = walk.length
    if (length != 10 || length%2 != 0) return false
    return walk.filter(x => x== 'n').length == walk.filter(x => x== 's').length && walk.filter(x => x== 'w').length == walk.filter(x => x== 'e').length
}