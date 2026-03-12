/* ================= BUTTON ================= */

.auth-button{

width:100%;

padding:12px;

background:#ff2a2a;

border:none;

border-radius:6px;

color:white;

cursor:pointer;

}

.outline-btn{

border:1px solid red;

padding:10px 20px;

border-radius:6px;

color:red;

text-decoration:none;

}

.outline-btn:hover{

background:red;

color:white;

}

/* ================= INPUT ================= */

.auth-input{

width:100%;

padding:12px;

background:#111;

border:1px solid #333;

border-radius:6px;

color:white;

}

/* ================= EXPLORE CARDS ================= */

.explore-grid{

display:grid;

grid-template-columns:repeat(3,1fr);

gap:20px;

}

.explore-card{

background:#111;

border:1px solid #333;

padding:20px;

border-radius:8px;

}

@media(max-width:900px){

.explore-grid{

grid-template-columns:1fr;

}

}