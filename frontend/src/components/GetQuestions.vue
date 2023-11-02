<template>
  <div v-loading="quesload">
    <div>
        <el-button @click="getquestions" v-if="first">点击生成AI问题</el-button>
        <el-button v-if="!first" @click="getquestions">重新生成问题</el-button>
    </div>
    <div v-html="compiledMarkdown">
    </div>
    <div v-if="error"> 
        <h1>
            {{ message }}
        </h1>
    </div>
    <div v-if="quesload" style="width:100%;height:200px"></div>
    <div class="buttons" v-if="compiledMarkdown">
        <el-button>保存回答</el-button>
    </div>
  </div>
</template>

<script>
import MarkdownIt from 'markdown-it';
import common from '@/assets/common/common';
import { ElMessage } from 'element-plus';
import axios from 'axios';

export default {
    name:'GetQuestions',
    data(){
        return{
            markdown:'',
            md:new MarkdownIt(),
            error:false,
            message:'',
            quesload:false,
            first:true,
        }
    },
    computed:{
        compiledMarkdown(){
            return this.md.render(this.markdown)
        }
    },
    methods:{
        clean(){
          this.markdown = ''
          this.error = false
          this.message = false
        },
        getquestions(){
        ElMessage.warning('AI正在依据PPT生成问题')
        this.quesload = true
        this.first = false
        try{
          axios.post(common.backend_prefix+'/getques')
          .then(
            response =>{
              console.log(response)
              if(response.data.message == 'fail'){
                console.log(response.data.message)
                ElMessage.error('响应失败')
                this.error = true
                this.message = response.data.result
                this.isloading = false
              }else{
                this.markdown2 = response.data.result
                this.successRestart = true
                ElMessage.success("成功响应！")
                this.isloading = false
              }
            }
          ).catch(
            error =>{
            this.error = true
              console.log(error);
              ElMessage.error('发生错误');
              this.message = error;
              this.quesload = false;
            }
          ).finally(
            () =>{
                this.quesload = false
            }
          );
      }catch(error){
        console.log(error);
        ElMessage.error('发生错误')
        this.message = error;
        this.error = true;
      }
    }
    }
}
</script>

<style>
.buttons{

}
</style>