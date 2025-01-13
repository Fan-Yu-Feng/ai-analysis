import { floatToFixed2 } from '@/utils'
import { isEmpty } from '@/utils/is'

// 格式化金额【分转元】
// @ts-ignore
export const fenToYuanFormat = (_, __, cellValue: any, ___) => {
  return `￥${floatToFixed2(cellValue)}`
}

export const renderSize = (value) => {
  if(null == value || value == '') {
    return "0 Bytes";
  }
  const unitArr = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  let index = 0;
  const srcsize = parseFloat(value);
  index = Math.floor(Math.log(srcsize) / Math.log(1024));
  const size = srcsize / Math.pow(1024, index);
  const _size = size.toFixed(2); //保留的小数位数
  return _size + unitArr[index];
}


/**
 * 将秒数转换为时:分:秒的格式字符串
 *
 * @param time 秒数
 * @returns 转换后的时:分:秒格式字符串
 */
export const sec2hs = (time) => {
  if (isEmpty(time)) return '00:00:00'
  // 转换为式分秒
  let h = '' + Math.min(parseInt(`${time / 60 / 60 % 24}`), 23)
  h = +h < 10 ? '0' + h : h
  let m = '' + Math.min(parseInt(`${time / 60 % 60}`), 59)
  m = +m < 10 ? '0' + m : m
  let s = '' + Math.min(Math.ceil(time % 60), 59)
    s = +s < 10 ? '0' + s : s
  // 作为返回值返回
  return h + ':' + m + ':' + s
}
