const skillsObj = [
	{
		domain: "frontend",
		skills: ["HTML - CSS", "Tailwind - Bootstrap", "jQuery - React.js"],
	},
	{ domain: "backend", skills: ["Express.js", "PostgreSQL", "APIs"] },
	{ domain: "languages", skills: ["JavaScript - Kotlin - Java"] },
	{
		domain: "tools",
		skills: ["Git - GitHub", "SCRUM", "English C2 - Native Spanish"],
	},
];

const projectsObj = [
	{
		title: "cryptolist",
		image: "./assets/img/cryptolist-1.jpg",
		description:
			"Android app for viewing a list of cryptocurrencies, managing user profiles, and starring coins by profile.",
		link: "https://github.com/armincano/cryptolist-app.git",
	},
	{
		title: "¡Ojala!",
		image: "./assets/img/ojala-1.png",
		description:
			"Landing page for the “¡Ojalá!” language learning mobile app, featuring contact forms for visitor inquiries and an admin login for managing submissions.<br />Proud of co-lead the Dev team using the Scrum framework.",
		link: "https://ojala.migracode.org/",
	},
];

$(document).ready(function () {
	// ANCHOR - Projects populating

	const projectsContainer = $("#projectsContainer");
	projectsObj.forEach((project, idx) => {
		const projectStructureItem = `
		<h3 class="wrap-text">
			# <span class="project-number">${idx + 1}</span>
		</h3>
		<div class="row">
		<div class="h-45 px-21 py-3 col-12 col-lg-6">
			<div class="card project-card-img h-100 p-2">
				<img
					src="${project.image}"
					class="img-fluid"
					alt="..."
				/>

				<div class="card-img-overlay text-end">
					<h5 class="card-title bordered-body-font">${project.title}</h5>
				</div>
			</div>
		</div>
		<div class="px-2 py-3 col-12 col-lg-6">
			<div class="card project-card-description px-2 py-3">
				<p class="card-text p-2">
					${project.description}
				</p>
				<hr />
				<p class="card-text px-2 project-link">
					<a
						href="${project.link}"
						target="_blank"
						class="link-offset-2 link-underline link-underline-opacity-0"
						>Visit ${project.title} ❤️</a
					>
				</p>
			</div>
		</div>
		
		${idx === projectsObj.length - 1 ? "" : "<div class='air-gap-small'></div>"}
	</div>`;
		projectsContainer.append(projectStructureItem);
	});

	// ANCHOR - Skills populating
	const skillsContainer = $("#skillsContainer");
	skillsObj.forEach((domain) => {
		const newDiv = $("<div class='col-12 col-lg-6'></div>")
		for (const key in domain.skills) {
			const bgColor =
				domain.domain === "frontend"
					? "bg-color-em1"
					: domain.domain === "backend"
					? "bg-color-em2"
					: domain.domain === "languages"
					? "bg-color-em3"
					: domain.domain === "tools"
					? "bg-color-em4"
					: "";
			const skillTab = `<div class="card skill-card d-flex flex-row align-items-center my-3">
					<div class="circle-3 p-3 ms-1 ${bgColor}"></div>
					<h4 class="card-text p-2">${domain.skills[key]}</h4>
				</div>`;
			newDiv.append(skillTab);
		}
		skillsContainer.append(newDiv);
	});

	// ANCHOR - Contact form
	const contactFormMessageInput = $("#contactFormMessageInput");
	const contactFormEmailInput = $("#contactFormEmailInput");
	$("#contactForm").on("submit", function (event) {
		event.preventDefault();
		$(".error").remove();
		$(".success").remove();
		const email = contactFormEmailInput.val().trim();
		const message = contactFormMessageInput.val().trim();

		let isValid = true;
		const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
		if (email === "") {
			isValid = false;
			contactFormEmailInput.after(
				"<div class='air-gap-small'></div><span class='error'>Email is required</span>"
			);
		} else if (!emailPattern.test(email)) {
			isValid = false;
			contactFormEmailInput.after(
				"<div class='air-gap-small'><span class='error'>Invalid email format</span>"
			);
		}

		if (message === "") {
			isValid = false;
			contactFormMessageInput.after(
				"<div class='air-gap-small'><span class='error'>Message is required</span>"
			);
		}

		if (isValid) {
			contactFormEmailInput.val("");
			contactFormMessageInput.val("");
			$("#contactForm").append(
				"<div class='air-gap-small'><span class='success'>Form submitted successfully</span>"
			);
		}
	});
});

$(document).ready(function () {
	const images = $(".project-card-img");

	const observer = new IntersectionObserver(
		(entries, observer) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					$(entry.target).addClass("in-view");
					observer.unobserve(entry.target);
				}
			});
		},
		{ threshold: 0.8 }
	);

	images.each(function () {
		observer.observe(this);
	});
});
