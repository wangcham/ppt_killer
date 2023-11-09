<template>
    <div>
        <div style="display: flex;flex-direction: row;">
            <el-input clearable class="input" v-model="content"></el-input>
            <el-button type="default" plain @click="search">查询</el-button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import common from '../assets/common/common'
import { ElMessage } from 'element-plus'
import {store} from '../store/store'
export default {
    name:'SearchOldData',
    data(){
        return{
            content:'',
            results:[], 
            store,
        }
    },
    methods:{
        async search(){
            if(this.content == ''){
                ElMessage.error('查询框不能为空')
                return
            }else{
                try{
                    await axios.post(common.backend_prefix+'/olddata',{'content':this.content})
                    .then(
                        response =>{
                            if(response.data.status == 'fail'){
                                ElMessage.error(response.data.message)
                                this.content = ''
                            }else{
                                this.results =  response.data
                                console.log("查询到对应的信息")
                                this.store.currentContent = this.results
                                this.$router.push({name:'/ShowOldData'});
                            }
                        }
                    )
                }catch{
                    error =>{
                        console.log(error)
                    }
                }
            }
    },
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