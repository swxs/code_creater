<template>
  <el-container>
    <el-aside width="200px">Aside</el-aside>
    <el-container>
      <el-header>
        <el-button type="text" @click="dialogFormVisible = true">创建</el-button>
      </el-header>
      <el-main>
        <el-table :data="tableData" style="width: 100%" max-height="250">
          <el-table-column fixed prop="en" label="en" width="150"></el-table-column>
          <el-table-column prop="cn" label="cn" width="120"></el-table-column>
          <el-table-column prop="number" label="number" width="120"></el-table-column>
          <el-table-column prop="last_time" label="last_time" width="120"></el-table-column>
          <el-table-column fixed="right" label="操作" width="120">
            <template slot-scope="scope">
              <el-button
                @click.native.prevent="updateRow(scope.$index, tableData)"
                type="text"
                size="small"
              >更新</el-button>
              <el-button
                @click.native.prevent="deleteRow(scope.$index, tableData)"
                type="text"
                size="small"
              >移除</el-button>
            </template>
          </el-table-column>
        </el-table>

        <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage2"
        :page-sizes="[100, 200, 300, 400]"
        :page-size="100"
        layout="sizes, prev, pager, next"
        :total="1000">
        </el-pagination>

        <el-dialog title="wordbook" :visible.sync="dialogFormVisible">
          <el-form :model="form">
            <el-form-item label="en" :label-width="formLabelWidth">
              <el-input v-model="form.en" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="cn" :label-width="formLabelWidth">
              <el-input v-model="form.cn" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="number" :label-width="formLabelWidth">
              <el-input v-model="form.number" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="last_time" :label-width="formLabelWidth">
              <el-input v-model="form.last_time" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="createRow()">确 定</el-button>
          </div>
        </el-dialog>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import {
  searchWord,
  selectWord,
  createWord,
  deleteWord,
} from '../api/Word.js'
import { MessageBox } from 'element-ui'

export default {
  name: 'home',
  data() {
    return {
      tableData: [],
      dialogFormVisible: false,
      formLabelWidth: '120px',
      form: {
        en: '',
        cn: '',
        number: '',
        last_time: ''
      }
    }
  },
  computed: {},
  components: {},
  created() {},
  async mounted() {
    let result = await searchWord({ order_by: '-created' })
    this.tableData = result.data
  },
  methods: {
    async createRow() {
      const result = await createWord(this.form)
      const data = await selectWord(result)
      this.tableData.splice(0, 0, data)
      this.form = {
        en: '',
        cn: '',
        number: '',
        last_time: ''
      }
      this.dialogFormVisible = false
    },
    async updateRow(index, rows) {
      
    },
    async deleteRow(index, rows) {
      const result = await deleteWord(rows[index].id)
      rows.splice(index, 1)
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
</style>
