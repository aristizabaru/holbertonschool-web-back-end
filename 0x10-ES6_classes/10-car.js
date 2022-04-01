export default class Car {
  constructor(brand, motor, color) {
    if (typeof brand !== 'string') throw new TypeError('brand must be a string');
    this._brand = brand;
    if (typeof motor !== 'string') throw new TypeError('motor must be a string');
    this._motor = motor;
    if (typeof color !== 'string') throw new TypeError('color must be a string');
    this._color = color;
  }

  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Clone = this.constructor[Symbol.species];
    return new Clone(this._brand, this._motor, this._color);
  }
}
