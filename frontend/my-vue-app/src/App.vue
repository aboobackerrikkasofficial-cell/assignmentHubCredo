<template>
  <div class="page-container">
    <router-view/>
  </div>
</template>

<style>
html,body,#app{
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}
.page-container{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  min-height: 100vh;
  background-image:url('/src/assets/backgroundforassignment.jpg');
  background-size: cover;
  background-repeat:no-repeat;
}

/* Mobile Responsive */
@media (max-width: 600px) {
  .page-container {
    display: flex;
    justify-content: center;
    margin: 0 auto;
    align-items: flex-start;
    padding-top: 60px;           
    padding-bottom: 20px;
    background-size: cover;
  }

  html, body, #app {
    height: auto;
    min-height: 100vh;
    overflow: hidden;
  }
}

  .popup-box {
    bottom: 70px !important;   
    padding: 6px 12px;
    font-size: 14px;
    transform: translateX(-10%);
    max-width: 90%;            
}
</style>
