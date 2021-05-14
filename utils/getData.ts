export default function(i: number,data: Array<''>, msg: string) {
    let including = data[i]
    if(msg.includes(including)) {
        return false
    } else {
        return true
    }
}