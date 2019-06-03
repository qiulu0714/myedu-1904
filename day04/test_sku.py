import allure
@allure.feature('商品模块')
class Test_order :
    @allure.story('添加商品')
    def test_order_add (self):
        assert '成功'  in '操作成功'

    @allure.story('删除订单')
    def test_order_to_wh(self):
        assert '成功' in '操作成功'