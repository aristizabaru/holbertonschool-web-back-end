export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string') throw new TypeError('name must be a string');
    this._name = name;
    if (typeof code !== 'string') throw new TypeError('code must be a string');
    this._code = code;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
