<template>
  <div class="container">
      <div class="all" v-loading="isloading">
        <div v-if="!fileuploaded" style="display:flex;flex-direction:column;">
          <h3 class="ppt-killer-text">PPT-killer</h3>
          <label for="file-input" class="file-input-label">
            <span>目前支持pptx文件 ( 太大的文件可能会导致AI回复失效！) </span>
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
      <div>
      </div>
    </div>
    <div v-if="isloading" style="display:flex;flex-direction:column;font-family: 'Source Han Sans SC', sans-serif; font-size: 15px; color: #333;">
      <h2>提示：</h2>
      <h4 style="margin-bottom:5px;margin-top:0;font-family: 'Source Han Sans SC', sans-serif;">如果上面的蓝色方框一直显示正在加载，不要着急，耐心等待一会儿，请不要关闭网页。</h4>
      <h4 style="margin-top:1px;font-family: 'Source Han Sans SC', sans-serif;">AI生成回答之后，会弹出消息提示框，并且在蓝色方框下方生成MarkDown格式内容。</h4>
      <h4 style="margin-top:0;">有些时候由于服务器和网络的原因，AI回复的速度会变得很慢，请保持耐心。</h4>
      <h3 style="margin-top:0;">MarkDown格式的效果类似这种的：</h3>
      <h3 style="margin-top:0;">我很喜欢U2乐队,为什么呢？</h3>
      <ul style="margin-top:0;">
        <li>因为他们的音乐很牛逼</li>
        <li>因为我喜欢玩原神</li>
        <li>因为我不是二次元</li>
      </ul>
      <p>这就是得到的效果，在得到AI回复后，本提示将会马上消失，祝你使用愉快!</p>
    </div>
      <div v-html="compiledMarkdown"
      style="margin-top:20px">
      </div>
    <div class="bottom">
      <h6 style="margin-right:30px">Made By Wangcham</h6>
      <el-link href="https://github.com/wangcham" type="success" target="_blank" :underline='false'>
      点击查看我的GitHub
        <el-icon style="margin-left:5px"><View /></el-icon>
      </el-link>
      <el-link @click="dialogvisible()" :underline='false' style="margin-left:30px;" type="primary">
        查看本站提示<el-icon style="margin-left:5px"><MagicStick /></el-icon>
      </el-link>
    </div>
    <el-dialog v-model="dialog" title="提示">
      <h4 style="margin-bottom:5px;margin-top:0;font-family: 'Source Han Sans SC', sans-serif;">如果上面的蓝色方框一直显示正在加载，不要着急，耐心等待一会儿，请不要关闭网页。</h4>
      <h4 style="margin-top:1px;font-family: 'Source Han Sans SC', sans-serif;">AI生成回答之后，会弹出消息提示框，并且在蓝色方框下方生成MarkDown格式内容。</h4>
      <h4 style="margin-top:0;">有些时候由于服务器和网络的原因(或者上传的文件很大)，AI回复的速度会变得很慢，请保持耐心。</h4>
      <h3 style="margin-top:0;">MarkDown格式的效果类似这种的：</h3>
      <el-divider/>
      <h3 style="margin-top:0;">我很喜欢U2乐队,为什么呢？</h3>
      <ul style="margin-top:0;">
        <li>因为他们的音乐很牛逼</li>
        <li>因为我喜欢玩原神</li>
        <li>因为我不是二次元</li>
      </ul>
      <el-divider/>
      <p style="margin-top:0;">以上就是得到的效果</p>
      <p style="margin-top:0;">如果你只有ppt文件，那么请使用外部网站或者Microsoft Powerpoint</p>
      <p style="margin-top:0;">将ppt文件转换成pptx文件，外部网站可以自己搜索去转换文件。</p>
      <h3>提示到这里就结束了，你很聪明，因为至少在使用前会去看看说明，感谢使用！</h3>
    </el-dialog>
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
      submitting:true,
      error:false,
      message:'',
      selectedFileName:'',
      dialog:false,
    };
  },
  computed:{
    compiledMarkdown(){
      return this.md.render(this.markdown)
    },
  },
  methods: {
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
      this.cancel();
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
              ElMessage.success("总结成功！")
              this.cancel()
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
      }
    }
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
</style>

