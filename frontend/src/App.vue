<template>
  <div class="all">
    <div v-if="!fileuploaded" style="display:flex;flex-direction:column;">
      <label for="file-input" class="file-input-label">
        <span>选择图片</span>
        <input id="file-input" type="file" accept="application/vnd.openxmlformats-officedocument.presentationml.presentation" @change="onFileChange">
      </label>
    </div>
    <div v-if="fileuploaded">
      <p>
        已选择文件:pptx
      </p>
    </div>
    <div>
      <el-button type="button" @click="submitUpload" v-if="fileuploaded">上传</el-button>
      <el-button type="button" @click="cancel" v-if="fileuploaded">清除内容</el-button>
    </div>
    <div v-pre> 
    <div v-html="compiledMarkdown" v-loading="isloading">
    </div>
    </div>
  </div>
</template>

<script>
import common from './assets/common/common'
import axios from 'axios';
import {ElMessage} from 'element-plus'
import MarkdownIt from 'markdown-it'

export default {
  name: 'UploadImage',
  data() {
    return {
      file: null,
      text: '',
      fileUrl: '',
      fileuploaded: false,
      md:new MarkdownIt(),
      markdown:'',
      isloading:false,
    };
  },
  computed:{
    compiledMarkdown(){
      return this.md.render(this.markdown)
    },
  },
  methods: {
    onFileChange(event) {
      const files = event.target.files;
      if (files.length > 0) {
        this.file = files[0];
        if (this.file) {
          this.fileUrl = URL.createObjectURL(this.file);
          this.fileuploaded = true;
          console.log(this.file)
        }
        console.log(this.file);
      }
    },
    cancel() {
      this.file = null;
      this.fileUrl = null;
      this.fileuploaded = false;
      this.text = ''
    },
    async submitUpload() {
      let formData = new FormData();
      formData.append('file',this.file);
      this.isloading = true;
      try {
        await axios.post(common.backend_prefix + '/getfile', formData)
          .then(response => {
            // 处理成功响应
            console.log(response);
            if (response.data.status === 'fail') {
              ElMessage.error(response.data.message)
              this.isloading = false
            } else {
              this.markdown = response.data.result
              ElMessage.success("总结成功！")
            }
          })
          .catch(error => {
            // 处理请求错误
            console.log(error);
          })
          .finally(() => {
            // 隐藏 loading 界面
            this.isloading = false
          });
      } catch (error) {
        // 处理 try 块中的错误
        console.log(error);
      }
    }
  }
}
</script>

<style>
.all {
  display: flex;
  flex-direction: column; /* 垂直居中 */
  align-items: center; /* 水平居中 */
  height: 100vh; /* 视口高度 */
}

/* 让按钮水平排列 */
.all > div:last-child {
  display: flex;
  gap: 10px; /* 按钮之间的间隔 */
}

</style>
