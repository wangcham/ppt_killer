<template>
    <div class="container">
      <div class="all" v-loading="isloading">
        <div v-if="!fileuploaded" style="display:flex;flex-direction:column;">
          <div style="display: flex;flex-direction: row;justify-content: space-between;">
            <div style="display:flex;flex-direction: row;">
              <img src="../assets/OIG.jpg" alt="PPT-killer-LOGO" style="width: 60px;height: 60px;margin-right: 10px;margin-top: 10px;margin-left: 10px;" class="logoimg"/>
              <div>
                <div style="margin-bottom: 30px;"></div>
                <h1 class="ppt-killer-text">PPT-killer</h1>
              </div>
            </div>
            <div style="margin-top: 10px;margin-bottom: 10px;">
              <SearchOldData></SearchOldData>
            </div>
          </div>
          <label for="file-input" class="file-input-label">
            <span>目前支持pptx文件 ( 太大的文件可能会导致AI回复失效！) ( ctrl+s保存AI回复 )
            <s></s> </span>
            <el-button type="primary" class="custom-file-input" id="button" style="margin-left:10px">
              点击这里开始上传文件
              <input id="file-input" type="file" accept="application/vnd.openxmlformats-officedocument.presentationml.presentation" @change="onFileChange" style="opacity: 0; position: absolute;height:100%;cursor: pointer;  " />
            </el-button>
          </label>
        </div>
        <div v-if="fileuploaded">
          <p style="" class="pp">
            已选择文件:{{selectedFileName}}
          </p>
        </div>
        <div v-if="submitting" class="buttons">
          <el-button type="button" @click="submitUpload" v-if="fileuploaded">询问AI</el-button>
          <el-button type="button" @click="cancel" v-if="fileuploaded">清除内容</el-button>
        </div>
        <div v-if="error">
          <h3 class="pp">
            发生错误 {{this.message}}
          </h3>
          <el-button type="default" @click="restart" style="margin-left:30px;margin-bottom:20px;">重新开始</el-button>
        </div>
        <div v-if="successRestart" style="margin-left: 30px;margin-bottom: 5px;">
          <el-button type="default" @click="restart">重新开始</el-button>
        </div>
      <div>
      </div>
    </div>
    <div v-if="isloading" style="display:flex;flex-direction:column;font-family: 'Source Han Sans SC', sans-serif; font-size: 15px; color: #333;">
      <LoadingTips></LoadingTips>
    </div>
    <div>
      <div v-html="compiledMarkdown"
      style="margin-top:20px">
      </div>
      <div v-if="compiledMarkdown">
        <el-button @click="ShowSave">保存总结</el-button>
      </div>
      <div style="margin-top: 10px;" v-if="compiledMarkdown">
        <GetQuestions :summarize="markdown"></GetQuestions>
      </div>
    </div>
    <div>
      <el-dialog v-model="save" title="保存AI生成的回答" destroy-on-close>
        <SaveAnswer :content="markdown" :type="type" @close-dialog="closedialog"></SaveAnswer>
      </el-dialog>
    </div>
    <!--占位-->
    <div v-if="!compiledMarkdown" style="display: flex;justify-content:center;">
      <TianliGenshin></TianliGenshin>
    </div>
    </div>
</template>

<script>
import common from '../assets/common/common'
import axios from 'axios';
import {ElMessage} from 'element-plus'
import MarkdownIt from 'markdown-it'
import LoadingTips from './LoadingTips.vue';
import SearchOldData from './SearchOldData.vue';
import GetQuestions from './GetQuestions.vue';
import SaveAnswer from './SaveAnswer.vue';
import TianliGenshin from './TianliGenshin.vue';
export default {
  name: 'GetSummarize',
  components:{
    LoadingTips,
    SearchOldData,
    GetQuestions,
    SaveAnswer,
    TianliGenshin,
  },
  data() {
    return {
      file: null,
      text: '',
      fileUrl: '',
      fileuploaded: false,
      md:new MarkdownIt(),
      markdown:'',
      isloading:false,
      submitting:true,
      error:false,
      message:'',
      selectedFileName:'',
      dialog:false,
      successRestart:false,
      showquestions:false,
      quesload:false,
      save:false,
      type:1,
    };
  },
  computed:{
    compiledMarkdown(){
      return this.md.render(this.markdown)
    },
  },
  methods: {
    closedialog(){
      this.save = false
    },
    ShowSave(){
      this.save = true;
    },
    showifgenerate(data){
      this.quesload = data;
    },
    dialogvisible(){
      this.dialog = true
    },
    onFileChange(event) {
      const files = event.target.files;
      if (files.length > 0) {
        this.file = files[0];
        if (this.file) {
          this.fileUrl = URL.createObjectURL(this.file);
          this.fileuploaded = true;
          this.selectedFileName = this.file.name;
          console.log(this.file)
        }
        console.log(this.file);
      }
    },
    cancel() {
      this.file = null;
      this.fileUrl = null;
      this.fileuploaded = false;
      this.text = '';
    },
    restart(){
      this.error = false;
      this.selectedFileName = '';
      this.fileuploaded = false;
      this.submitting = true;
      this.text = '';
      this.markdown = '';
      this.cancel();
      this.successRestart = false;
      this.markdown2 = '';
    },
    async submitUpload() {
      let formData = new FormData();
      formData.append('file',this.file);
      this.isloading = true;
      this.submitting = true;
      ElMessage.warning("AI正在生成内容")
      try {
        await axios.post(common.backend_prefix + '/getfile', formData)
          .then(response => {
            // 处理成功响应
            console.log(response);
            if (response.data.status === 'fail') {
              ElMessage.error(response.data.message)
              this.isloading = false
              this.error = true
              this.message = response.data.result
            } else {
              this.markdown = response.data.result
              this.successRestart = true;
              ElMessage.success("成功响应！")
              this.file = null;
              this.fileUrl = null;
              this.text = '';
            }
          })
          .catch(error => {
            // 处理请求错误
            console.log(error);
            this.message = error;
            this.error = true;
          })
          .finally(() => {
            // 隐藏 loading 界面
            this.isloading = false;
            this.submitting = false;
          });
      } catch (error) {
        // 处理 try 块中的错误
        console.log(error);
        this.message = error;
        this.error = true;
        this.isloading = false
      }
    },
    //请求问题与答案
    getques(){
        this.showquestions = true;
    },
  }
  }
</script>

<style>
  .all {
    background-color: #3498db; /* 设置背景色为蓝色 */
    border: 1px solid #2980b9; /* 添加细边框 */
    border-radius: 8px; /* 使边框角圆润一些 */
    /* padding: 20px; */
    position: relative;
    width: 100%;
  }

  .answer{
    margin-top: 5px;
    background-color: #dbf6fb;
    border:1px solid #3498db;
    border-radius: 6px;
    padding: 20px;
    width: 100%;
  }

  .pp {
    margin-left: 30px;
    color: #fff; /* 设置段落文字颜色为白色 */
  }

  .el-button {
    background-color: #2980b9; /* 设置按钮背景色为稍深的蓝色 */
    border: none;
    color: #fff; /* 设置按钮文字颜色为白色 */
    border-radius: 4px; /* 圆润按钮的角 */
    margin-right: 10px;
  }

  .el-button:hover {
    background-color: #1f67a6; /* 设置按钮的鼠标悬停颜色 */
  }

  .el-button:disabled {
    background-color: #ccc; /* 设置按钮的禁用状态颜色 */
    color: #333; /* 设置文字颜色为灰色 */
  }

.file-input-container {
  display: flex;
  align-items: center;
}

.ppt-killer-text {
  position: relative;
  top: 0;
  margin-top: 10px;
  margin-left: 10px;
  font-size: 20px; /* 调整字体大小 */
  color: #fff; /* 设置字体颜色为白色 */
  margin-right: 20px; /* 调整"ppt-killer"文本和输入框之间的间距 */
}

.file-input-label {
  display: inline-block;
  padding: 10px;
  background-color: #2980b9;  
  margin: 20px;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
}

.custom-file-input {
  border: 2px solid #2980b9;
  background-color: #dbf6fb;
  padding: 5px;
  border-radius: 4px;
  color: #2980b9;
  cursor: pointer;
}
#button{
  background-color: #fff; /* 设置按钮背景色为白色 */
  border: none;
  color: #2980b9; /* 设置按钮文字颜色为蓝色 */
  border-radius: 4px; /* 圆润按钮的角 */
  margin-right: 10px;
}
.buttons{
  margin-left: 30px;
  margin-top: 30px;
  margin-bottom: 30px;
}
.bottom{
  position: absolute;
  margin-bottom: 10px;
  margin-left:30px;

  display:flex;
  flex-direction: row;
  justify-content: center;

}
.fill{
  margin-top:30px;
  margin-bottom: 30px;
}
.logoimg{
border-radius: 10px;

-webkit-border-radius: 10px;

-moz-border-radius: 10px;
}

.loadingpart{
  width: 100%;
  height:200px;
}
</style>