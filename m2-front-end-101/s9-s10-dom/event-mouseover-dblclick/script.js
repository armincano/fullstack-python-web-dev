const text1 = document.querySelector('#text1');
const text2 = document.querySelector('#text2');
const img = document.querySelector('#caja2 img');
const lastText = document.querySelector('#caja3 p');

text1.addEventListener("mouseover", () => text2.classList.remove('hidden'));
text1.addEventListener("mouseout", () => text2.classList.add('hidden'));

img.addEventListener("mouseover", () => img.classList.replace('normal-width', 'full-width'));
img.addEventListener("mouseout", () => img.classList.replace('full-width', 'normal-width'));

lastText.addEventListener("dblclick", () => lastText.classList.toggle('large-text'));