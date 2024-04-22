document.addEventListener("DOMContentLoaded", function() {
    const homeContent = document.getElementById("homeContent");
    const activitiesContent = document.getElementById("activitiesContent");
    const classesContent = document.getElementById("classesContent");
    const createTestBtn = document.getElementById("createTestBtn");
    const submitCodeBtn = document.getElementById("submitCodeBtn");
    const menuIcon = document.getElementById("menuIcon");
    const dropdownContent = document.getElementById("dropdownContent");

    // Toggle between different tabs
    document.querySelectorAll("nav ul li a").forEach(function(tab) {
        tab.addEventListener("click", function() {
            document.querySelector("nav ul li a.active").classList.remove("active");
            this.classList.add("active");
            switchContent(this.innerText.toLowerCase());
        });
    });

    // Toggle between different contents
    function switchContent(tabName) {
        if (tabName === "home") {
            homeContent.style.display = "block";
            activitiesContent.style.display = "none";
            classesContent.style.display = "none";
        } else if (tabName === "activities") {
            homeContent.style.display = "none";
            activitiesContent.style.display = "block";
            classesContent.style.display = "none";
        } else if (tabName === "classes") {
            homeContent.style.display = "none";
            activitiesContent.style.display = "none";
            classesContent.style.display = "block";
        }
    }

    // Toggle dropdown menu
    menuIcon.addEventListener("click", function() {
        dropdownContent.style.display = (dropdownContent.style.display === "block") ? "none" : "block";
    });

    // Close dropdown menu when clicking outside
    document.addEventListener("click", function(event) {
        if (!event.target.matches("#menuIcon")) {
            dropdownContent.style.display = "none";
        }
    });

    // Example: Button action
    createTestBtn.addEventListener("click", function() {
        alert("creating a test")
    });

    // Initialize content to home page
    switchContent("home");

    submitCodeBtn.addEventListener("click", function(){
        alert("Submiting a code...")
    });

});


