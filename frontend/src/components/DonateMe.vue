<template>
    <div style="display: flex; flex-direction: column;">
        <h3>是这样的，服务器和Api Key都是需要定期充值的，捐赠的钱会用来充值这些必需品，来支持后续的服务</h3>
        <div style="display: flex;flex-direction: row;justify-content: space-around;">
            <img src="../assets/ali_pay.jpg" alt="支付宝捐赠"  style="margin-right: 10px;"/>
            <img src="../assets/wechat_pay.jpg" alt="微信支付" />
        </div>
    </div>
</template>

<script>
export default {
    name:'DonateMe',
}
</script>

<style>
img{
    width: 200px;
    height: 270px;
}
</style>