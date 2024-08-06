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

$(document).ready(function () {

	// ANCHOR - Skills populating
	const skillsContainer = $("#skillsContainer");
	skillsObj.forEach((domain) => {
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
			const skillTab = `<div class="card skill-card d-flex flex-row align-items-center ps-2 mx-3 my-3">
						<div class="circle-3 px-3 ${bgColor}"></div>
						<h3 class="card-text p-2">${domain.skills[key]}</h3>
					</div>`;
			skillsContainer.append(skillTab);
		}
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
			contactFormEmailInput.after("<div class='air-gap-small'></div><span class='error'>Email is required</span>");
		} else if (!emailPattern.test(email)) {
			isValid = false;
			contactFormEmailInput.after("<div class='air-gap-small'><span class='error'>Invalid email format</span>");
		}

		if (message === "") {
			isValid = false;
			contactFormMessageInput.after("<div class='air-gap-small'><span class='error'>Message is required</span>");
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
