
const fileInput = document.getElementById("profile-img-file-input");
const profileImg = document.getElementById("profile-img");

fileInput.addEventListener("change", () => {
    const chosedFile = fileInput.files[0];
    profileImg.src = URL.createObjectURL(chosedFile);
});

const handleProfileUpdate = () => {
    const username = document.getElementById("userName").value
    const fullname = document.getElementById("fullName").value
    const about = document.getElementById("about").value
    const email = document.getElementById("email").value
    const location = document.getElementById("location").value
    const languages = document.getElementById("languages").value
    const skills = document.getElementById("skills").value
    alert("hello")
    const user = {
        "username": username,
        "fullname": fullname,
        "about": about,
        "email": email,
        "loc": location,
        "languages": languages,
        "skills": skills
    };
    console.log(user);
}
