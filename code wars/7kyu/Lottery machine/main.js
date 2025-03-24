// With regexp
function lottery(str){
    let arr = str.match(/[0-9]/g);
    return arr ? [...new Set(arr)].join('') : 'One more run!';
 }
// can be shorten with
const lot =  str => (arr = str.match(/[0-9]/g)) ? [...new Set(arr)].join('') : 'One more run!';
// Without regexp
const lottery = str => {
    return [...new Set([...str])].filter(e => e >= 0 && e <= 9).join('') || 'One more run!';
}