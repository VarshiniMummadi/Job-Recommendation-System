
// Job Recommendation System Frontend Script

document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("jobForm");
    const skillsInput = document.querySelector("input[name='skills']");

    form.addEventListener("submit", function (event) {

        let skills = skillsInput.value.trim();

        if (skills === "") {
            alert("Please enter your skills before searching for jobs.");
            event.preventDefault();
            return;
        }

        skillsInput.value = skills.toLowerCase();

    });

});