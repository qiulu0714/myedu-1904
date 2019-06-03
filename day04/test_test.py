import allure
@allure.feature('订单模块')
class Test_df :
    @allure.story('下订单')
    def test_order_fg (self):
        assert '成功'  in '操作成功'

    @allure.story('订单发货')
    def test_order_to_wh(self):
        assert '成功' in '操作成功'