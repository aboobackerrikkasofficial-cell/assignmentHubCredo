<template>
    <div class="signup-box">
        <h1>Create Your Account</h1>
        <div class="signup-inputs">
            <input type="text" placeholder="Full Name" v-model="fullname">
            <input type="email" placeholder="Email" v-model="email">
            <input type="password" placeholder="Password" v-model="password">
            <input type="password" placeholder="Confirm Password" v-model="confirm_password">
        </div>
        <button class="signup-btn" @click="signUpUser">Sign Up</button>
        <p class="login-area">Already have an account? <router-link to='/'>Login Page</router-link></p>
        
        <transition name="slide-up">
            <div v-if="showPopup" class="popup-box">
                <p>{{ popupmessage }}</p>
            </div>
        </transition>
    </div>
</template>

<script setup>
    import axios from 'axios';
    import {ref} from 'vue';

    const fullname=ref("");
    const email=ref("");
    const password=ref("");
    const confirm_password=ref("");
    const showPopup=ref(false);
    const popupmessage=ref("");

    const signUpUser = async () =>{
        try{
            const res=await axios.post("https://assignmenthubcredo-4.onrender.com/signup",{
                fullname:fullname.value,
                email:email.value,
                password:password.value,
                confirm_password:confirm_password.value
            });

            popupmessage.value=res.data.message;
            showPopup.value=true;

            setTimeout(() => {showPopup.value = false;}, 3000);

        }catch(err){
            popupmessage.value=err.response?.data?.message || "Server not reachable";
            showPopup.value=true;

            setTimeout(() => {showPopup.value = false;}, 3000);
        }
    };
</script>

<style scoped>
.signup-box{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    width: 500px;
    padding: 20px 80px;
    border-radius: 10px;
    margin: 0;
    background: white;
}
.signup-box h1{
    color: black;
    font-size: 34px;
    font-weight: 800;
    font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.signup-box .signup-inputs{
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 100%;
}
.signup-box .signup-inputs input{
    padding: 15px 10px;
    border-radius: 10px;
    box-shadow: 2px 4px 20px rgba(198, 255, 211, 0.155);
    background:rgba(159, 255, 159, 0.297);
    border: none;
    color: rgb(0, 44, 0);
    font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    font-weight: 600;
    font-size: 14px;
}
.signup-box .signup-inputs input:focus{
    outline: 2px solid #00440285;
}
.signup-box .login-area{
    color: black;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 600;
}
.signup-box .signup-btn{
    background: rgb(2, 174, 2);
    font-size: 18px;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 600;
    text-align: center;
    width: 300px;
    outline: none;
}
.signup-box .signup-btn:hover{
    background: rgb(0, 70, 0);
    transition: background 0.2s ease-in;
}
.login-area a{
    color: rgb(0, 100, 0);
}
.login-area a:hover{
    color: #001601;
}
.popup-box {
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  background:rgb(0, 174, 0);
  color: white;
  padding: 2px 20px;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  z-index: 9999;
}
.slide-up-enter-from,
.slide-up-leave-to {
  opacity: 0;
  transform: translate(-50%, 150px);
}
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.3s ease;
}
.slide-up-enter-to,
.slide-up-leave-from {
  opacity: 1;
  transform: translate(-50%, 0px);
}

/* Mobile Responsive */

@media (max-width: 600px) {
.signup-box {
display: flex;
flex-direction: column;
align-items: center;
gap: 20px;
width: 100%;
max-width: 350px;           
padding: 20px;     
border-radius: 10px;
margin: 0 auto;
background: white;
}

.signup-box h1 {
font-size: 26px;
text-align: center;
}

.signup-box .signup-inputs {
gap: 15px;
width: 100%;
}

.signup-box .signup-inputs input {
padding: 12px 10px;
font-size: 14px;
}
}

</style>