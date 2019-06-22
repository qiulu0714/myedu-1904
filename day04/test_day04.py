#
#
# class Rich_list():
#     def __init__(self,name ,firm ,ranking,job):
#         self.name =name
#         self.firm = firm
#         self.ranking = ranking
#         self.job = job
#
#     def rank_1(self):
#         print('我叫%s,我创办了%s,我排在%s,我是%s'%(self.name,self.firm,self.ranking,self.job))
#
#     def eat(self):
#         print(self.name+'吃早餐')
#
# class JD(Rich_list):
#     def rank_2(self):
#         print('我叫%s,我创办了%s,我排在%s,我是%s'%(self.name,self.firm,self.ranking,self.job))
#         self.eat()
#
# if __name__ == '__main__':
#     # rich_list = Rich_list('马云', '阿里巴巴', '世界第一', '执行董事')
#     # rich_list.rank_1()
#     # rich_list.eat()
#     jd = JD('刘强东', '京东', '世界第二', '董事长')
#     jd.rank_2()
#     jd.eat()
# -----------------------------------------------------------------------------------------
import allure

@allure.feature('订单模块')
class Test_order:

    @allure.story('下订单')
    def test_order_add(self):
        assert '成功' in '操作成功'

    def test_order_o_wh(self):
        assert '成功' in '操作成功'



