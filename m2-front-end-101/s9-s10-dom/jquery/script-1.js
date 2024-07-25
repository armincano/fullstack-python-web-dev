$(document).ready(function () {
	// 1. A button click event that changes the text of a paragraph element
	$("#changeTextBtn").click(function () {
		$("#text1").text("Hello from jQuery");
	});

	// 2. A button click event that toggle the paragraph element between diplay and hide
	$("#toggleTextBtn").click(function () {
		$("#text2").toggle();
	});

	// 3. Attach an event handler to be fired when the mouse enters a div element. The event changes the background color of the div element<br>Concatenate an event handler to be fired when the mouse leaves an element. The event changes the background color to the previous one.
	$("#squareToggleColorDiv")
		.mouseenter(function () {
			$(this).css("background-color", "green");
		})
		.mouseleave(function () {
			$(this).css("background-color", "red");
		});

	// 4. Animate a div element to move to the right when the mouse enters the element. Notice that the 'position' css property is set to 'relative' so we can work with the 'float' propery with value 'left' and use the left side of the box as reference to move. There is also a delay before executing the second event handler's code.
	$("#squareMoveRightDiv")
		.mouseenter(function () {
			$(this).animate({ left: 100, width: 50, height: 50 });
		})
		.mouseleave(function () {
			setTimeout(() => {
				$(this).animate({ left: 0, width: 100, height: 100 });
			}, 2000);
		});

	// 5. Listen for the form submit event, prevent the default form submission, and validate the form input data.
	$("#form1").on("submit", function (event) {
        event.preventDefault()
		let isValid = true;
        $(".error").remove();
        $(".success").remove();
        $("#username").empty();
        $("#username").empty();

        const username = $("#username").val().trim();
        const email = $("#email").val().trim();
        
		// validate username
		if (username === "") {
			isValid = false;
			$("#username").after(
				"<span class='error'>Username is required</span>"
			);
		}

        // validate password
		const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        if(email === "") {
            isValid = false;
            $("#email").after("<span class='error'>Email is required</span>")
        }else if (!emailPattern.test(email)) {
			isValid = false;
			$("#email").after(
				"<span class='error'>Invalid email format</span>"
			);
		}

        if (isValid) {
            // $("#form1").html("<span class='success'>Form submitted successfully</span>") // replace the innerHTML of form1
            $("#form1").append("<span class='success'>Form submitted successfully</span>")
        }

	});
});
