<template>
  <div style="display: flex;flex-direction: row;">
    <el-input clearable class="input" v-model="content"></el-input>
    <el-button type="default" plain @click="search">查询</el-button>
  </div>
</template>

<script>
// import axios from 'axios';

export default {
    name:'SearchOldData',
    data(){
        return{
            content:'',
            results:'', 
        }
    },
    methods:{
        async search(){
            
        }
    }
}
</script>

<style>
.input{
    width: 250px;
    height: 30px;
    margin-right: 5px;
}
</style>