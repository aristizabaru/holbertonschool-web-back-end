export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') throw new TypeError('sizemust be a number');
    this._size = size;
    if (typeof location !== 'string') throw new TypeError('locationmust be a string');
    this._location = location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'number') {
      return this._size;
    }
    if (hint === 'string') {
      return this._location;
    }

    return null;
  }
}
