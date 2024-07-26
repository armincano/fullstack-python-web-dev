/* Vanilla JS
const text1 = document.querySelector('#text1');
const text2 = document.querySelector('#text2');
const img = document.querySelector('#caja2 img');
const lastText = document.querySelector('#caja3 p');

text1.addEventListener("mouseover", () => text2.classList.remove('hidden'));
text1.addEventListener("mouseout", () => text2.classList.add('hidden'));

img.addEventListener("mouseover", () => img.classList.replace('normal-width', 'full-width'));
img.addEventListener("mouseout", () => img.classList.replace('full-width', 'normal-width'));

lastText.addEventListener("dblclick", () => lastText.classList.toggle('large-text')); */

// jQuery
$(document).ready(function () {
	$("#text1")
		.mouseover(function () {
			$("#text2").removeClass("hidden");
		})
		.mouseleave(function () {
			$("#text2").addClass("hidden");
		});

	$("#caja2 img")
		.mouseover(function () {
			$(this).removeClass("normal-width").addClass("full-width");
		})
		.mouseleave(function () {
			$(this).removeClass("full-width").addClass("normal-width");
		});

	$("#caja3 p").dblclick(function () {
		$(this).toggleClass("large-text");
	});
});
