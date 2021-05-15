export default function (i: number, data: Array<"">, msg: string) {
  if (msg.includes(data[i)) {
    return false;
  } else {
    return true;
  }
}
