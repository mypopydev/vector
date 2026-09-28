-- 把译稿里的几类围栏 Div 还原成 header.tex 定义的 LaTeX 环境。
-- 用法：pandoc --lua-filter=tools/infobox.lua
--
-- 注意：**只能有一处 `function Div(el)`**。Lua 里同名的全局函数是后定义覆盖前者，
-- 本文件原先写了三个 `function Div(el)`（infobox / displayeq），结果只有最后一个
-- （displayeq）生效，知识框与署名行两个分支从来没执行过——知识框一直以普通段落
-- 渲染，页面上根本看不出是「框」（实测第 38 页）。改成一张分派表；新增 Div 类型
-- 时往 ENVS 里加一项即可，不要再另写一个 function Div。

local ENVS = {
  infobox = "infobox",        -- 知识框（tcolorbox，灰底）
  attribution = "attribution",-- 推荐语署名行（右对齐）
  displayeq = "displayeq",    -- 非 MathML 的行间公式（居中）
}

function Div(el)
  for class, env in pairs(ENVS) do
    if el.classes:includes(class) then
      local out = { pandoc.RawBlock("latex", "\\begin{" .. env .. "}") }
      for _, block in ipairs(el.content) do
        table.insert(out, block)
      end
      table.insert(out, pandoc.RawBlock("latex", "\\end{" .. env .. "}"))
      return out
    end
  end
  return el
end
