/*!
   item post scripts for user
  */
$("body").on('click', '.u_like', function() {like = $(this); item = like.parents('.infinite-item');pk = item.attr("user-id");uuid = item.attr("item-id");dislike = like.next().next();$.ajax({url: "/votes/user_like/" + uuid + "/" + pk + "/",type: 'POST',data: {'obj': pk},success: function(json){like.find("[data-count='like']").text(json.like_count); like.toggleClass('btn_success btn_default'); like.next().html('').load("/window/u_like_window/" + uuid + "/" + pk + "/");dislike.find("[data-count='dislike']").text(json.dislike_count); dislike.removeClass('btn_danger').addClass("btn_default"); dislike.next().html('').load("/window/u_dislike_window/" + uuid + "/" + pk + "/")}});return false;});
$("body").on('click', '.u_dislike', function() {dislike = $(this); item = dislike.parents('.infinite-item');pk = item.attr("user-id");uuid = item.attr("item-id");like = dislike.prev().prev();$.ajax({url: "/votes/user_dislike/" + uuid + "/" + pk + "/", type: 'POST', data: {'obj': pk},success: function(json) {like.find("[data-count='like']").text(json.like_count); like.removeClass('btn_success').addClass("btn_default"); like.next().html('').load("/window/u_like_window/" + uuid + "/" + pk + "/");dislike.find("[data-count='dislike']").text(json.dislike_count); dislike.toggleClass('btn_danger btn_default'); dislike.next().html('').load("/window/u_dislike_window/" + uuid + "/" + pk + "/")}});return false;});

$("body").on('click', '.u_like2', function() {like = $(this);pk = like.data('pk');uuid = like.data('uuid');dislike = like.next().next();$.ajax({url: "/votes/user_comment/" + uuid + "/" + pk + "/like/", type: 'POST', data: {'obj': pk},success: function(json) {like.find("[data-count='like']").text(json.like_count); like.toggleClass('btn_success btn_default'); like.next().html('').load("/window/u_comment_like_window/" + uuid + "/" + pk + "/");dislike.find("[data-count='dislike']").text(json.dislike_count); dislike.removeClass('btn_danger').addClass("btn_default"); dislike.next().html('').load("/window/u_comment_dislike_window/" + uuid + "/" + pk + "/")}});return false;});
$("body").on('click', '.u_dislike2', function() {dislike = $(this);pk = dislike.data('pk');uuid = dislike.data('uuid');like = dislike.prev().prev();$.ajax({url: "/votes/user_comment/" + uuid + "/" + pk + "/dislike/", type: 'POST', data: {'obj': pk},success: function(json) {like.find("[data-count='like']").text(json.like_count); like.removeClass('btn_success').addClass("btn_default"); like.next().html('').load("/window/u_comment_like_window/" + uuid + "/" + pk + "/");dislike.find("[data-count='dislike']").text(json.dislike_count); dislike.toggleClass('btn_danger btn_default'); dislike.next().html('').load("/window/u_comment_dislike_window/" + uuid + "/" + pk + "/")}});return false;});

$('body').on('click', '.u_itemComment', function() {button1 = $(this);form1 = button1.parent().parent().parent();upload_block = form1.find(".upload_block");$.ajax({url: '/user/post-comment/', data: new FormData($(form1)[0]),contentType:false,cache:false,processData:false,type:'POST',success:function(data){ $(".form-control-rounded").val(""); form1.parent().prev().append(data); upload_block.empty()},error: function(data) { $.toast({heading: 'Ошибка',text: 'Для публикации комментария нужно написать что-нибудь и/или вставить изображение(ия)',showHideTransition: 'fade',icon: 'error'}); },});return false;});
$('body').on('click', '.u_replyComment', function() {button = $(this);form2 = button.parent().parent().parent().parent();block = form2.parent();upload_block = form2.find(".upload_block");reply_stream = block.next().next();pk = button.data('pk');uuid = button.data('uuid');$.ajax({url: '/user/reply-comment/' + uuid + "/" + pk + "/", data: new FormData($(form2)[0]), contentType: false, cache: false, processData: false, type: 'POST',success: function(data) { $(".form-control-rounded").val(""); reply_stream.append(data); reply_stream.addClass("replies_open"); block.hide(); upload_block.empty(); },error: function(data) { $.toast({heading: 'Ошибка',text: 'Для публикации ответа нужно написать что-нибудь и/или вставить изображение(ия)',showHideTransition:'fade',icon:'error'})},});return false;});
$('body').on('click', '.u_replyParentComment', function() {button = $(this);form3 = button.parent().parent().parent().parent();block = form3.parent();upload_block = form3.find(".upload_block");pk = button.data('pk');uuid = button.data('uuid');reply_stream = block.parents('.stream_reply_comments');$.ajax({url: '/user/reply-comment/' + uuid + "/" + pk + "/",data: new FormData($(form3)[0]),contentType: false,cache: false,processData: false,type: 'POST',success: function(data) { $(".form-control-rounded").val(""); reply_stream.append(data); block.hide(); upload_block.empty();},error: function(data) { $.toast({heading: 'Ошибка',text: 'Для публикации ответа нужно написать что-нибудь и/или вставить изображение(ия)',showHideTransition: 'fade',icon: 'error'}) },});return false;});

$('body').on('click', '.item_user_remove', function() {remove = $(this);uuid = remove.parents(".infinite-item").attr("item-id");$.ajax({url: "/user/delete/" + uuid + "/",success: function(data) {$(remove).parents('.card').hide();$('.activefullscreen').hide();$.toast({heading: 'Информация',text: 'Запись успешно удалена!',showHideTransition: 'fade',icon: 'info'})}});});
$('body').on('click', '.item_user_fixed', function() {fixed = $(this);uuid = fixed.parents(".infinite-item").attr("item-id");$.ajax({url: "/user/fixed/" + uuid + "/",success: function(data) {fixed.parent().html("<span class='dropdown-item item_user_unfixed'>Открепить</span>");$.toast({heading: 'Информация',text: 'Запись закреплена!',showHideTransition: 'fade',icon: 'info'})}});});
$('body').on('click', '.item_user_unfixed', function() {unfixed = $(this);uuid = unfixed.parents(".infinite-item").attr("item-id");$.ajax({url: "/user/unfixed/" + uuid + "/",success: function(data) {unfixed.parent().html("<span class='dropdown-item item_user_fixed'>Закрепить</span>");$.toast({heading: 'Информация',text: 'Запись откреплена!',showHideTransition: 'fade',icon: 'info'})}});});
$('body').on('click', '.item_user_off_comment', function() {off = $(this);uuid = off.parents(".infinite-item").attr("item-id");$.ajax({url: "/user/off_comment/" + uuid + "/",success: function(data) {off.parent().html("<span class='dropdown-item item_user_on_comment'>Включить комментарии</span>");$.toast({heading: 'Информация',text: 'Комментарии выключены!',showHideTransition: 'fade',icon: 'info'})}});});
$('body').on('click', '.item_user_on_comment', function() {on = $(this);uuid = on.parents(".infinite-item").attr("item-id");$.ajax({url: "/user/on_comment/" + uuid + "/",success: function(data) {on.parent().html("<span class='dropdown-item item_user_off_comment'>Выключить комментарии</span>");$.toast({heading: 'Информация',text: 'Комментарии включены!',showHideTransition: 'fade',icon: 'info'})}});});
$('body').on('click', '.js-textareacopybtn', function() {btn = $(this);link = btn.find('.js-copytextarea');link.focus();link.select();try {var successful = document.execCommand('copy');var msg = successful ? 'successful' : 'unsuccessful';console.log('Copying text command was ' + msg);} catch (err) {console.log('Oops, unable to copy');}});


/*!
   item post scripts for community
  */
$("body").on('click', '.c_like', function() {like = $(this);item = like.parents('.infinite-item');uuid = item.attr("item-id");pk = item.attr("community-id"); dislike = like.next().next();$.ajax({url: "/votes/community_like/" + uuid + "/" + pk + "/", type: 'POST', data: {'obj': pk},success: function(json) {like.find("[data-count='like']").text(json.like_count);like.toggleClass('btn_success btn_default');like.next().html('').load("/window/c_like_window/" + uuid + "/" + pk + "/");dislike.find("[data-count='dislike']").text(json.dislike_count);dislike.removeClass('btn_danger').addClass("btn_default");dislike.next().html('').load("/window/c_dislike_window/" + uuid + "/" + pk + "/")}}); return false;});

$("body").on('click', '.c_dislike', function() {dislike = $(this); item = dislike.parents('.infinite-item');uuid = item.attr("item-id"); var pk = item.attr("community-id");like = dislike.prev().prev();$.ajax({url: "/votes/community_dislike/" + uuid + "/" + pk + "/", type: 'POST', data: {'obj': pk},success: function(json) {like.find("[data-count='like']").text(json.like_count);like.removeClass('btn_success').addClass("btn_default");like.next().html('').load("/window/c_like_window/" + uuid + "/" + pk + "/");dislike.find("[data-count='dislike']").text(json.dislike_count); dislike.toggleClass('btn_danger btn_default');dislike.next().html('').load("/window/c_dislike_window/" + uuid + "/" + pk + "/")}}); return false;});

$("body").on('click', '.c_like2', function() {like = $(this);pk = like.data('pk');uuid = like.data('uuid');dislike = like.next().next();$.ajax({url: "/votes/community_comment/" + uuid + "/" + pk + "/like/", type: 'POST', data: {'obj': pk},success: function(json) {like.find("[data-count='like']").text(json.like_count);like.toggleClass('btn_success btn_default');like.next().html('').load("/window/c_comment_like_window/" + uuid + "/" + pk + "/");dislike.find("[data-count='dislike']").text(json.dislike_count); dislike.removeClass('btn_danger').addClass("btn_default");dislike.next().html('').load("/window/c_comment_dislike_window/" + uuid + "/" + pk + "/")}}); return false;});

$("body").on('click', '.c_dislike2', function() {dislike = $(this);pk = dislike.data('pk');uuid = dislike.data('uuid');like = dislike.prev().prev();$.ajax({url: "/votes/community_comment/" + uuid + "/" + pk + "/dislike/",type: 'POST',data: { 'obj': pk },success: function(json) {like.find("[data-count='like']").text(json.like_count); like.removeClass('btn_success').addClass("btn_default");like.next().html('').load("/window/c_comment_like_window/" + uuid + "/" + pk + "/");dislike.find("[data-count='dislike']").text(json.dislike_count); dislike.toggleClass('btn_danger btn_default');dislike.next().html('').load("/window/c_comment_dislike_window/" + uuid + "/" + pk + "/")}});return false;});
