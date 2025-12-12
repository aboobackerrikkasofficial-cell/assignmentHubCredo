<template>
    <div class="login-box">
        <h1>Login Page</h1>
        <div class="inputs-areas">
            <input type="email" placeholder="Email" v-model="email">
            <input type="password" placeholder="Password" v-model="password">
        </div>
        <button class="login-btn" @click="loginUser">Login</button>
        <p class="signup-area">Don't have an account? <router-link to="/signup">Sign Up</router-link></p>
        <transition name="slide-up">
            <div v-if="showPopup" class="popup-box">
            <p>{{ popupmessage }}</p>
            </div>
        </transition>
    </div>
</template>

<script setup>
    import axios from 'axios';
    import {onMounted, ref} from 'vue';
    import {useRouter} from 'vue-router';

    const router=useRouter();
    const email=ref("");
    const password=ref("");
    const showPopup=ref(false);
    const popupmessage=ref("");

    const loginUser = async () =>{
        try{
            const res=await axios.post("https://assignmenthubcredo-4.onrender.com/login",{
                email:email.value,
                password:password.value
            });

            localStorage.setItem("fullname",res.data.fullname)
            localStorage.setItem("msg",res.data.message);

            router.replace("/dashboard");

        }catch(err){
            popupmessage.value=err.response?.data?.message || "Server not reachable";
            showPopup.value=true;

            setTimeout(() => {showPopup.value = false;}, 3000);
        }
    };

onMounted(() =>{
    const fullNameFromSession=localStorage.getItem("fullname");
    if (fullNameFromSession){
        router.replace("/dashboard")
    }
});
</script>

<style scoped>
.login-box{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    width: 500px;
    padding: 40px;
    border-radius: 10px;
    margin: 0;
    background: white;
}
.login-box h1{
    color: black;
    font-size: 34px;
    font-weight: 800;
    font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
}
.login-box .inputs-areas{
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 100%;
}
.login-box .inputs-areas input{
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
.login-box .inputs-areas input:focus{
    outline: 2px solid #00440285;
}
.login-box .signup-area{
    color: black;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 600;
}
.login-box .login-btn{
    background: rgb(2, 174, 2);
    font-size: 18px;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 600;
    text-align: center;
    width: 300px;
    outline: none;
}
.login-box .login-btn:hover{
    background: rgb(0, 70, 0);
    transition: background 0.2s ease-in;
}
.signup-area a{
    color: rgb(0, 100, 0);
}
.signup-area a:hover{
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
  .login-box {
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

  .login-box h1 {
    font-size: 26px;
    text-align: center;
  }

  .login-box .inputs-areas {
    gap: 15px;
  }

  .login-box .inputs-areas input {
    padding: 12px 10px;
    font-size: 14px;
    border-radius: 8px;
  }

  .login-box .login-btn {
    width: 100%;
    font-size: 16px;
    padding: 12px 0;
    border-radius: 8px;
  }

  .signup-area {
    font-size: 14px;
    text-align: center;
  }

  .popup-box {
    font-size: 14px;
    padding: 6px 15px;
    bottom: 20px;
  }
}

</style>