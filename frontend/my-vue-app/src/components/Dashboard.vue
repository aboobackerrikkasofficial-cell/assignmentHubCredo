<template>
  <div class="dashboard">
    <nav  class="navigation-bar">
        <h4>Dashboard</h4>
        <button @click="logOut">Logout</button>
    </nav>
    <h1>Welcome <span>{{ fullname }}</span></h1>

    <transition name="slide-up">
      <div v-if="showPopup" class="popup-box">
        <p>{{ popupmessage }}</p>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter,useRoute } from 'vue-router';

const router = useRouter();
const route=useRoute();
const fullname=ref("");
const showPopup = ref(false);
const popupmessage = ref("");


onMounted(() => {

    const nameFromSession=localStorage.getItem("fullname");
    const msgFromSession = localStorage.getItem("msg");

    if(!nameFromSession){
        router.replace("/")
    }else{
        fullname.value=nameFromSession
    }
    if (msgFromSession) {
    popupmessage.value = msgFromSession;
    showPopup.value = true;

    setTimeout(() => {
      showPopup.value = false;
      localStorage.removeItem("msg");
    }, 2000);
  }

    window.history.pushState(null, "",window.location.href);
    window.onpopstate = function () {
        window.history.pushState(null, "",this.window.href);
    };
});

function logOut(){
    localStorage.removeItem("fullname");
    router.replace("/");
}
</script>

<style>
.dashboard{
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
    height: 100%;
}
.dashboard h4{
    font-size: 20px;
}
.navigation-bar{
    position: fixed;      
    top: 0;                
    left: 0;               
    width:100%;           
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    background: white;
    color: black;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15); 
    z-index: 1000;
    box-sizing: border-box;
}
.navigation-bar button{
    padding: 10px 30px;
    margin: 0;
}
.dashboard h1{
    text-align: top;
}
.dashboard h1 span{
    color: rgb(0, 74, 0);
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

  .navigation-bar {
    padding: 10px 15px;
  }

  .navigation-bar h4 {
    font-size: 18px;
  }

  .navigation-bar button {
    padding: 8px 18px;
    font-size: 14px;
    border-radius: 6px;
  }

  .dashboard h1 {
    font-size: 22px;
    text-align: center;
    margin-top: 120px;   /* space below fixed navbar */
    padding: 0 15px;
  }

  .dashboard h1 span {
    font-size: 22px;
    color: rgb(0, 74, 0);
  }

  .popup-box {
    font-size: 14px;
    padding: 6px 15px;
    bottom: 20px;
  }
}

</style>
