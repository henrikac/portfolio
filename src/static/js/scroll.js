const arrowLink = document.querySelector('#arrow');
const navLinks = document.querySelectorAll('.nav-link');
const aboutSection = document.querySelector('#about');

const addScrollEvent = (from, to) => {
	from.addEventListener('click', e => {
		e.preventDefault();

		to.scrollIntoView({ behavior: 'smooth' });
	});
};

addScrollEvent(arrowLink, aboutSection);

navLinks.forEach(navLink => {
	const navLinkText = navLink.innerText.toLowerCase();
	const section = document.getElementById(navLinkText);

	addScrollEvent(navLink, section);
});
