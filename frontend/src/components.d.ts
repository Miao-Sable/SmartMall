// Vant 组件全局类型声明（完整引入时，模板中可直接使用 van-* 组件）
declare module 'vue' {
  export interface GlobalComponents {
    VanButton: (typeof import('vant'))['Button']
    VanCell: (typeof import('vant'))['Cell']
    VanCellGroup: (typeof import('vant'))['CellGroup']
    VanCheckbox: (typeof import('vant'))['Checkbox']
    VanCheckboxGroup: (typeof import('vant'))['CheckboxGroup']
    VanEmpty: (typeof import('vant'))['Empty']
    VanField: (typeof import('vant'))['Field']
    VanForm: (typeof import('vant'))['Form']
    VanGrid: (typeof import('vant'))['Grid']
    VanGridItem: (typeof import('vant'))['GridItem']
    VanIcon: (typeof import('vant'))['Icon']
    VanImage: (typeof import('vant'))['Image']
    VanLoading: (typeof import('vant'))['Loading']
    VanNavBar: (typeof import('vant'))['NavBar']
    VanNoticeBar: (typeof import('vant'))['NoticeBar']
    VanTabbar: (typeof import('vant'))['Tabbar']
    VanTabbarItem: (typeof import('vant'))['TabbarItem']
    VanTag: (typeof import('vant'))['Tag']
  }
}

export {}
