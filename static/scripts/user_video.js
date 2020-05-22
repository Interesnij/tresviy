on('#ajax', 'click', '.u_video_detail', function() {
  var uuid, pk, loader;
  counter = this.getAttribute('data-counter');
  parent = this.parentElement.parentElement;
  pk = parent.getAttribute('data-pk');
  uuid = parent.getAttribute('data-uuid');
  loader = document.getElementById("video_loader");
  open_fullscreen("/video/user/basic_list/" + pk + "/" + uuid + "/", loader);
  video_saver = document.body.querySelector("#video_id_saver");
  video_player_id = video_saver.getAttribute('data-video');
  video_saver.setAttribute('data-video', video_player_id + "a");
  setTimeout(function() {
    load_video_playlist(video_player_id + "a", counter);
    video_player.addListener(FWDUVPlayer.READY, onReady);
    function onReady(){
    console.log("video player ready");
    setTimeout(function() {video_player.playVideo(counter);video_player.play()}, 1000);
    }
  }, 500);
});
on('#ajax', 'click', '.u_video_list_detail', function() {
  var uuid, pk, loader;
  counter = this.getAttribute('data-counter');
  parent = this.parentElement.parentElement;
  pk = parent.getAttribute('data-pk');
  uuid = parent.getAttribute('data-uuid');
  loader = document.getElementById("video_loader");
  open_fullscreen("/video/user/list/" + pk + "/" + uuid + "/", loader);
  video_saver = document.body.querySelector("#video_id_saver");
  video_player_id = video_saver.getAttribute('data-video');
  video_saver.setAttribute('data-video', video_player_id + "a");
  setTimeout(function() {
    load_video_playlist(video_player_id + "a", counter);
    video_player.addListener(FWDUVPlayer.READY, onReady);
    function onReady(){
    console.log("video player ready");
    setTimeout(function() {video_player.playVideo(counter);video_player.play()}, 1000);
    }
  }, 500);
});

on('body', 'click', '.video_fullscreen_resize', function() {
  video_window = document.querySelector(".video_fullscreen");
  video_window.classList.add("video_fullscreen_resized", "draggable");
  document.body.querySelector(".video_btn_big").style.display = "none";
  document.body.querySelector(".video_btn_small").style.display = "block";
  get_resize_screen();
  dragElement(document.querySelector(".draggable"));

});
on('body', 'click', '.video_fullscreen_normal', function() {
  video_window = document.querySelector(".video_fullscreen");
  video_window.style.top = "0"; video_window.style.left = "auto";
  video_window.classList.remove("video_fullscreen_resized", "draggable");
  document.body.querySelector(".video_btn_small").style.display = "none";
  document.body.querySelector(".video_btn_big").style.display = "block";
  get_normal_screen()
});

on('#ajax', 'click', '.user_video_list_create', function() {
  var parent, pk, uuid, loader
  parent = this.parentElement.parentElement.parentElement.parentElement.parentElement;
  uuid = parent.getAttribute("item-uuid");
  loader = document.getElementById("stat_loader");
  open_fullscreen("/stat/item/" + uuid + "/", loader)
});

on('#ajax', 'click', '.user_video_list_create', function() {
  var parent, pk, uuid, loader
  parent = this.parentElement.parentElement.parentElement.parentElement.parentElement;
  uuid = parent.getAttribute("item-uuid");
  loader = document.getElementById("stat_loader");
  open_fullscreen("/stat/item/" + uuid + "/", loader)
});

on('body', 'click', '#create_video_album_btn', function() {
  _this = this;
  pk = _this.getAttribute("data-pk");
  form_data = new FormData(document.querySelector("#create_video_album"));
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'POST', "/video/progs/create_list/", true );

  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    console.log("vse ok")
    }};
  link.send(form_data);
})