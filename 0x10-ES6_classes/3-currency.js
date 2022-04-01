export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') throw new TypeError('Code must be a string');
    this._code = code;
    if (typeof name !== 'string') throw new TypeError('Name must be a string');
    this._name = name;
  }

  // getters
  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  // setters
  set code(code) {
    if (typeof code !== 'string') throw new TypeError('Code must be a string');
    this._code = code;
  }

  set name(name) {
    if (typeof name !== 'string') throw new TypeError('Name must be a string');
    this._name = name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
