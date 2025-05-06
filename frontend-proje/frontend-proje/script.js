async function handleFormSubmit() {
  try {
    const arac_km = parseFloat(document.getElementById("arac_km").value);
    const toplu_km = parseFloat(document.getElementById("toplu_km").value);
    const ucak_km = parseFloat(document.getElementById("ucak_km").value);
    const et = document.getElementById("et").value === "true";
    const elektrik = document.getElementById("elektrik").value === "true";
    const alisveris = document.getElementById("alisveris").value === "true";

    const payload = {
      arac_km, toplu_km, ucak_km, et, elektrik, alisveris,
      date: new Date().toISOString(),
      user_id: 1
    };

    const response = await fetch("http://localhost:8000/calculate_footprint", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!response.ok) throw new Error("Sunucudan hata döndü");

    const data = await response.json();
    const params = new URLSearchParams({
      carbon_score: data.carbon_score,
      comment: data.comment
    });

    window.open("sonuc.html?" + params.toString(), "_blank");
  } catch (error) {
    alert("Bir hata oluştu: " + error.message);
  }
}



fetch("http://127.0.0.1:8000/register", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    name: "Gizem",
    email: "gizem@example.com",
    password: "1234"
  }),
});

// Other important pens.
// Map: https://codepen.io/themustafaomar/pen/ZEGJeZq
// Dashboard: https://codepen.io/themustafaomar/pen/jLMPKm

let dropdowns = document.querySelectorAll('.navbar .dropdown-toggler')
let dropdownIsOpen = false

// Handle dropdown menues
if (dropdowns.length) {
  // Usually I don't recommend doing this (adding many event listeners to elements have the same handler)
  // Instead use event delegation: https://javascript.info/event-delegation
  // Why: https://gomakethings.com/why-event-delegation-is-a-better-way-to-listen-for-events-in-vanilla-js
  // But since we only have two dropdowns, no problem with that. 
  dropdowns.forEach((dropdown) => {
    dropdown.addEventListener('click', (event) => {
      let target = document.querySelector(`#${event.target.dataset.dropdown}`)

      if (target) {
        if (target.classList.contains('show')) {
          target.classList.remove('show')
          dropdownIsOpen = false
        } else {
          target.classList.add('show')
          dropdownIsOpen = true
        }
      }
    })
  })
}

// Handle closing dropdowns if a user clicked the body
window.addEventListener('mouseup', (event) => {
  if (dropdownIsOpen) {
    dropdowns.forEach((dropdownButton) => {
      let dropdown = document.querySelector(`#${dropdownButton.dataset.dropdown}`)
      let targetIsDropdown = dropdown == event.target

      if (dropdownButton == event.target) {
        return
      }

      if ((!targetIsDropdown) && (!dropdown.contains(event.target))) {
        dropdown.classList.remove('show')
      }
    })
  }
})

// Open links in mobiles
function handleSmallScreens() {
  document.querySelector('.navbar-toggler')
    .addEventListener('click', () => {
      let navbarMenu = document.querySelector('.navbar-menu')

      if (!navbarMenu.classList.contains('active')) {
        navbarMenu.classList.add('active')
      } else {
        navbarMenu.classList.remove('active')
      }
    })
}

handleSmallScreens()

  function openNewPage() {
    // Yeni sayfayı açmak için window.open kullanıyoruz
    window.open("sonuc.html", "_blank");  // _blank yeni sekmede açar
  }
