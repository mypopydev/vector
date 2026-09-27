-- pandoc 默认会把 ::: {.infobox} 这个 Div 整个丢掉（已实测确认），
-- 这里把它还原成 header.tex 里定义的 infobox 环境（tcolorbox）。
-- 用法：pandoc --lua-filter=tools/infobox.lua
function Div(el)
  if el.classes:includes("infobox") then
    local out = { pandoc.RawBlock("latex", "\\begin{infobox}") }
    for _, block in ipairs(el.content) do
      table.insert(out, block)
    end
    table.insert(out, pandoc.RawBlock("latex", "\\end{infobox}"))
    return out
  end
  return el
end

-- 非 MathML 的行间公式（原书用 <i>/<sub>/<sup> 排版）包成居中环境
function Div(el)
  if el.classes:includes("displayeq") then
    local out = { pandoc.RawBlock("latex", "\\begin{displayeq}") }
    for _, block in ipairs(el.content) do
      table.insert(out, block)
    end
    table.insert(out, pandoc.RawBlock("latex", "\\end{displayeq}"))
    return out
  end
  return el
end
