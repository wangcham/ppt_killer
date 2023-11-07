<template>
    <div>
        <el-input v-model="token" placeholder="请输入自己的密钥"></el-input>
        <el-button style="margin-top: 20px;" @click="submit">提交</el-button>
        <div>
            <el-dialog title="未查询到此密钥，是否要创建新密钥保存结果？" v-model="CreateNewToken">
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
        },
        async submit(){
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
                        ElMessage.error('AI生成回答失败')
                    }
                    if(response.data.code == '3'){
                        ElMessage.success('保存成功')
                        this.$emit('close-dialog')
                    }
                    if(response.data.status == 'fail'){
                        ElMessage.error('服务器发生错误')
                        console.log(response.data.message)
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