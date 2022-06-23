/*Downloaded from https://www.codeseek.co/jedrzejchalubek/coverflow-carousel-with-glidejs-MwPBGd */
function coverflow(i, el) {
  el.removeClass("pre following")
    .nextAll()
    .removeClass("pre following")
    .addClass("following")
    .end()
    .prevAll()
    .removeClass("pre following")
    .addClass("pre");
}

$("#Glide").glide({
  type: "slider",
  startAt: 3,
  animationDuration: 500,
  paddings: "25%",
  afterInit: function (event) {
    coverflow(event.index, event.current);
  },
  afterTransition: function (event) {
    coverflow(event.index, event.current);
  },
});
