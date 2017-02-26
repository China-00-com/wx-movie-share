define("mlist/main",["index/main","weui/searchbar","utils/imageutil"],function(require,exports){function i(){var i=$("div.movie-item").width();$("div.movie-item").height(1.4*i)}function e(){a=!1;var i=$("div.load-all");i.length>0?($loadmore=$("div.weui-loadmore"),$loadmore.length>0&&($("span.weui-loadmore__tips").text(""),$("i.weui-loading").hide(),$loadmore.addClass("weui-loadmore_line weui-loadmore_dot"),$loadmore.show())):$("div.weui-loadmore").hide()}function n(n,o){$.get("mlist/loadmore",{start:o,ms:n}).done(function(n){var o=$(n);o.appendTo($("div.movie__panel")),i(),l.lazyLoad(o),e()}).fail(function(){e()})}function o(){var i=$("div.load-all");if(i.length>0)return $loadmore=$("div.weui-loadmore:hidden"),$loadmore.length>0&&($("span.weui-loadmore__tips").text(""),$("i.weui-loading").hide(),$loadmore.addClass("weui-loadmore_line weui-loadmore_dot"),$loadmore.show()),void 0;if(!a){a=!0,$("span.weui-loadmore__tips").text("\u6b63\u5728\u52a0\u8f7d"),$("i.weui-loading").show(),$("div.weui-loadmore").removeClass("weui-loadmore_line weui-loadmore_dot"),$("div.weui-loadmore").show();var e=$("div.movie-item").length,o=$("div.weui-bar__item_on").data("role")||"movie";n(o,e)}}function t(){$(document).scroll($("div.weui-footer"),function(){var i=$(this).scrollTop(),e=$(this).height(),n=$(window).height();0>=e-i-1.5*n&&o()})}var a,d=require("../index/main"),l=require("../utils/imageutil"),r=function(){d.init(),t()};exports.init=r}),define("index/main",["weui/searchbar","utils/imageutil"],function(require,exports){function i(){var i="\u6b22\u8fce\u5149\u4e34\uff0c\u5929\u5929\u770b\u7247\u597d\u5fc3\u60c5\uff01",e=(new Date).getHours();1==e?i="\u4e00\u70b9\u591a\u5566\uff01\u5fd8\u4e86\u4f11\u606f\u5417?":2==e?i="\u5de5\u4f5c\u72c2\uff0c\u8be5\u4f11\u606f\u4e86\u54d2\uff01":3==e?i="\u5348\u591c\u4e09\u70b9\uff01\u7761\u89c9\u5427??!":4==e?i="\u51cc\u6668\u56db\u70b9\u591a\uff0c\u6ce8\u610f\u8eab\u4f53\u54d2":5==e?i="\u60a8\u662f\u521a\u8d77\u5e8a\u8fd8\u662f\u8fd8\u6ca1\u7761\u554a?":6==e?i="\u65e9\u4e0a\u597d\uff01\u65b0\u4e00\u5929\u53c8\u5f00\u59cb\u5566!":7==e?i="\u5403\u8fc7\u65e9\u996d\u4e86\u5417\uff1f\u4e48\u4e48\u54d2":8==e||9==e||10==e?i="\u65e9\uff01\u53c8\u662f\u5fd9\u788c\u7684\u4e00\u5929\uff01":11==e?i="\u5feb\u4e2d\u5348\u5566\uff0c\u51c6\u5907\u505a\u996d\u4e86\u5440\uff01":12==e?i="\u4e2d\u5348\u597d\uff01\u4f60\u5403\u996d\u4e86\u5417\uff1f":13==e||14==e?i="\u4e0b\u5348\u597d\uff0c\u51c6\u5907\u51c6\u5907\u8981\u4e0a\u73ed\u4e86\uff01":15==e||16==e||17==e?i="\u4e48\u4e48\u54d2,\u4e0b\u5348\u597d\uff01":18==e||19==e?i="\u5403\u665a\u996d\u4e86\u6ca1\uff1f\u4e48\u4e48\u54d2":20==e||21==e||22==e?i="\u522b\u5de5\u4f5c\u4e86\uff0c\u770b\u7535\u5f71\u770b\u7761\u89c9\u54d2":23==e?i="\u4e0d\u65e9\u4e86\uff0c\u5feb\u4f11\u606f\u5427!":0==e&&(i="\u5348\u591c\u65f6\u5206\uff0c\u6ce8\u610f\u8eab\u4f53\u54d2!"),$("span.say-hello-tips").text(i)}function e(){var i=$("div.movie-item").width();$("div.movie-item").height(1.4*i)}function n(){var i=$("div.movie-container");i&&i.length>0&&i.delegate("a.btn-more","click",function(){var i=$(this),e=i.data("role");e&&0!=e.trim().length&&(window.location.href="./mlist?ms="+e)})}function o(){var i=$("a.favor__me");i&&i.length>0&&i.click(function(){$("div.mask-window.closable").show()})}function t(){var i=$("div.weui-navbar__item");i&&i.length>0&&i.click(function(){var i=$(this),e=i.data("role");e&&0!=e.trim().length||(e="movie"),window.location.href="./mlist?ms="+e})}function a(){var i=$("div.movie-container");i&&i.length>0&&i.delegate("div.movie-item","click",function(){var i=$(this).data("mid");i&&parseInt(i)>0&&(window.location.href="./mplay?mid="+i)})}function d(){$("i.close__window").click(function(){$("div.mask-window.closable").hide()})}function l(){$("#search_input").keydown(function(i){if(13==i.which){var e=$.trim($(this).val());e.length>0&&setTimeout(function(){window.location.href="./mfind?mf="+e},100)}})}var r=require("../weui/searchbar"),c=require("../utils/imageutil"),u=function(){n(),o(),t(),d(),a(),$(document).ready(function(){i(),r.init("#search_bar","#search_text","#search_input","#search_clear","#search_cancel"),c.lazyLoad($("div.weui-tab__panel")),e(),l()}),$(window).resize(function(){e()}),document.body.addEventListener("touchmove",function(i){"none"!=$("div.mask-window").css("display")&&i.preventDefault()},!1)};exports.init=u}),define("weui/searchbar",[],function(require,exports){var i=function(i,e,n,o,t,a){function d(){c.hide(),s.val("")}function l(){d(),r.removeClass("weui-search-bar_focusing"),u.show()}var r=$(i),c=$(a),u=$(e),s=$(n),m=$(o),h=$(t);u.on("click",function(){r.addClass("weui-search-bar_focusing"),s.focus()}),s.on("blur",function(){this.value.length||l()}).on("input",function(){this.value.length?c.show():c.hide()}),m.on("click",function(){d(),s.focus()}),h.on("click",function(){l(),s.blur()})};exports.init=i}),define("utils/imageutil",[],function(require,exports){exports.lazyLoad=function(i){var e=i.find("img[data-src]");e.each(function(){var i=$(this),e=i.attr("src"),n=i.data("src"),o=i.parent("div[data-role=img-wrapper]");o&&0!=o.length&&(e&&0!==(e=e.trim()).length?o.css("background-image","url("+n+")"):(i.on("load",function(){o.css("background-image","url("+n+")")}),i.attr("src",n)))})}});