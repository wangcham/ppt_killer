<template>
    <div>
        <div class="head">
                <div style="display:flex;flex-direction: row;" class="pptkiller">
                    <img src="../assets/OIG.jpg" style="width: 60px;height: 60px;margin-right: 10px;margin-top: 10px;margin-left: 10px;margin-bottom: 10px;"/>
                    <div style="display:flex;flex-direction: column;">
                        <div style="margin-left: 10px;margin-bottom: 10px;"></div>
                        <h2 style="font-family: Verdana, Geneva, Tahoma, sans-serif;color:cornflowerblue">PPT-killer</h2>
                    </div>
                </div>
                <h1 style="font-family: Georgia, 'Times New Roman', Times, serif;">搜索到的结果:</h1>
        </div>
        <div style="display: flex;justify-content: center;flex-direction: column;" class="used">
            <div v-for="result in results" :key="result" class="outer">
                <div class="inner" @click="goToDetailPage(result.content)">
                    <h3 class="title">{{ result.type === 1 ? '总结':'问题' }}</h3>
                    <h3> : {{ result.content.length > 60 ? result.content.substring(0, 60) + '...' : result.content }}</h3>
                </div>
                <hr />
            </div>
            <div style="margin-top:50px"></div>
        </div>
    </div>
</template>

<script>
import {store} from '../store/store.js'
export default {
    name:'ShowOldData',
    data(){
        return{
            // results:[
            //     {
            //         "type":1,
            //         "content":'in the name of love,what more in the name of love'
            //     },
            //     {
            //         "type":2,
            //         "content":'hey jude,don\'t make it bad,take a sad song,and make it better'
            //     }
            // ],
            store,
            results:[],
        }
    },
    mounted(){
        this.results = this.store.currentContent
    },
    methods:{
        goToDetailPage(content){
            this.SaveContentToStore(content)
            this.$router.push({name:'/DetailPage'});
        },
        SaveContentToStore(content){
            this.store.content = content
        }
    }
}
</script>

<style>
.head{
    align-items: center;
    display: flex;
    background-color: aliceblue;
    justify-content: center;
    align-items: center;
}


.head > div:first-child {
    position: absolute;
    left: 10px;
}


.head > h1 {
    margin-left: auto;
    margin-right: auto;
}

.outer {
    display: flex;
    justify-content: center;
    flex-direction: column;
}

.used {
    position: relative;
}
.inner{
    display: flex;
    flex-direction: row;
    cursor: pointer;
    transition: background-color 0.3s ease;
    width:100%;
}
.inner:hover{
    background-color: floralwhite;
}
.title{
    color:cornflowerblue;
}
</style>