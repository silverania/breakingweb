function getData(valuenext){
this.value=valuenext;
}

getData.prototype.publicMethod = function () {
  return (this.value);
};
