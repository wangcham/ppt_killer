<template>
    <div>
        <el-input v-model="token" placeholder="请输入自己的密钥"></el-input>
        <el-button style="margin-top: 20px;" @click="submit">提交</el-button>
        <div>
            <el-dialog title="未查询到此密钥，是否要创建此密钥为新密钥并保存结果？" v-model="CreateNewToken">
                <div style="display: flex;flex-direction: row;">
                    <el-button @click="submitagain" style="margin-right: 10px;">确认</el-button>
                    <el-button @click="CreateNewToken=false">取消</el-button>
                </div>
            </el-dialog>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import common from '../assets/common/common'
import { ElMessage } from 'element-plus'
export default {
    name:'SaveAnswer',
    props:{
        content:String,
        type:Number,
    },
    data(){
        return{
            token:'',
            CreateNewToken:false,
        }
    },
    methods:{
        async submitagain(){
            //未查询到token，进行确认
            try{
                await axios.post(common.backend_prefix+"/saveagain",{
                    'content':this.content,
                    'type':this.type,
                    'token':this.token,   
                }).then(
                    response =>{
                        if(response.data.status == 'fail'){
                            ElMessage.error('保存失败')
                            console.log(response.data.message)
                        }else{
                            ElMessage.success(response.data.message)
                            this.CreateNewToken = false
                            this.$emit('close-dialog')
                        }
                    }
                ).catch(
                    error =>{
                        console.log(error)
                        ElMessage.error("发生错误"+error)
                        this.CreateNewToken = false
                    }
                ).finally(
                    this.CreateNewToken = false
                )
            }catch{
                error =>{
                    console.log(error)
                    ElMessage.error('发生错误：'+error)
                }
            }
        },
        async submit(){
            if(this.token == ''){
                ElMessage.error('密钥不能为空！')
                return
            }
            if(this.token.length <= 6){
                ElMessage.error('密钥不能少于6位')
                return
            }
            try{
                await axios.post(common.backend_prefix+'/saveanswer',{
                'content':this.content,
                'type':this.type,
                'token':this.token,
            })
            .then(
                response =>{
                    if(response.data.code == '1'){
                        console.log('未查询到此token')
                        this.CreateNewToken = true
                    }
                    if(response.data.code == '2'){
                        ElMessage.error(response.data.message)
                    }
                    if(response.data.code == '3'){
                        ElMessage.success('保存成功')
                        this.$emit('close-dialog')
                    }
                }
            ).catch(
                error =>{
                    console.log(error)
                    ElMessage.error('发生错误')
                }
            ).finally(
                console.log('finally')
            )
            }catch{
                err =>{
                    console.log(err)
                }
                ElMessage.error('发生错误')
            }       
        },
    },

}
</script>

<style>

</style>