# 연구 개요 1쪽 PDF(researchprep/연구개요_20261026.pdf)를 만드는 스크립트.
#
# 사용법:
#   1) 나눔고딕(OFL) 글꼴 세 개를 한 폴더에 내려받는다.
#      https://raw.githubusercontent.com/google/fonts/main/ofl/nanumgothic/NanumGothic-Regular.ttf
#      https://raw.githubusercontent.com/google/fonts/main/ofl/nanumgothic/NanumGothic-Bold.ttf
#      https://raw.githubusercontent.com/google/fonts/main/ofl/nanumgothic/NanumGothic-ExtraBold.ttf
#   2) python3 make_overview_pdf.py <글꼴 폴더> <출력 PDF 경로>
#
# 필요 패키지: reportlab. 생성 후 pypdf로 쪽수가 1인지 확인한다.

import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

font_dir, out = sys.argv[1], sys.argv[2]
pdfmetrics.registerFont(TTFont("NG", f"{font_dir}/NanumGothic-Regular.ttf"))
pdfmetrics.registerFont(TTFont("NGB", f"{font_dir}/NanumGothic-Bold.ttf"))
pdfmetrics.registerFont(TTFont("NGX", f"{font_dir}/NanumGothic-ExtraBold.ttf"))
pdfmetrics.registerFontFamily("NG", normal="NG", bold="NGB", italic="NG", boldItalic="NGB")

title = ParagraphStyle("t", fontName="NGX", fontSize=16, leading=21, textColor=black, alignment=TA_LEFT)
sub = ParagraphStyle("s", fontName="NG", fontSize=9.2, leading=13, textColor=black)
h = ParagraphStyle("h", fontName="NGX", fontSize=12.5, leading=16, textColor=black, spaceBefore=10, spaceAfter=4.5)
body = ParagraphStyle("b", fontName="NG", fontSize=9.7, leading=15.2, textColor=black, alignment=TA_JUSTIFY, spaceAfter=5)
bullet = ParagraphStyle("bl", parent=body, leftIndent=13, firstLineIndent=-10, spaceAfter=4.5, alignment=TA_LEFT)
subbul = ParagraphStyle("sb", parent=body, leftIndent=27, firstLineIndent=-10, spaceAfter=2.5, alignment=TA_LEFT)
item = ParagraphStyle("i", parent=body, leftIndent=20, firstLineIndent=-20, spaceAfter=4.5)
rq = ParagraphStyle("rq", fontName="NGB", fontSize=10.3, leading=16.3, textColor=black, alignment=TA_JUSTIFY)
note = ParagraphStyle("n", fontName="NG", fontSize=8.2, leading=11.5, textColor=black)

def B(text, style=bullet, mark="•"):
    return Paragraph(f"{mark}&nbsp;&nbsp;{text}", style)

S = []
S.append(Paragraph("AI 기반 복제·대체와 미디어 소프트웨어 플랫폼의 권력 구조 변화", title))
S.append(Spacer(1, 3))
S.append(Paragraph("연구 개요 초안 · 고려대학교 미디어학과 석사과정 김권택 · 2026-10-26", sub))
S.append(Spacer(1, 5))
S.append(HRFlowable(width="100%", thickness=0.8, color=black, spaceBefore=0, spaceAfter=2))

S.append(Paragraph("1. 연구 배경", h))
S.append(B("<b>디지털 소프트웨어 소유권의 약화</b>"))
S.append(B("소니는 2028년 1월부터 PlayStation 신작의 디스크 생산을 중단한다고 발표했다(2026.7).", subbul, "-"))
S.append(B("PlayStation 게임 판매에서 디지털 비중은 이미 82~85%다.", subbul, "-"))
S.append(B("Adobe는 숨겨진 해지 수수료 문제로 미국 법무부와 FTC에 제소되었다(2024).", subbul, "-"))
S.append(B("<b>AI에 의한 복제·대체 비용과 숙련 장벽의 하락</b>"))
S.append(B("N64 게임 Snowboard Kids가 AI 에이전트로 84일 만에 소스 코드로 복원되었다.", subbul, "-"))
S.append(B("AI로 디컴파일한 헤일로, 콜 오브 듀티 등의 브라우저 이식판이 잇달아 공개되었다(2026.9~10).", subbul, "-"))
S.append(B("AI 에이전트용 역공학 도구 REA가 GitHub 스타 32만 개를 넘겼고, Claude로 만든 Adobe 제품 7종의 대체품(알파 수준)이 공개되었다.", subbul, "-"))
S.append(B("<b>플랫폼 대응의 분화</b>"))
S.append(B("억제: 닌텐도와 테이크투는 삭제 요청을 이어 가고 있다.", subbul, "-"))
S.append(B("재봉쇄: 소니는 싱글플레이 퍼스트파티 게임을 다시 독점으로 돌리고 디스크를 없애기로 했다.", subbul, "-"))
S.append(B("흡수와 억제의 병행: 마이크로소프트는 Xbox Labs를 세웠지만, 자회사 액티비전과 베데스다는 AI로 만든 프로젝트를 내리게 했다.", subbul, "-"))
S.append(B("도구 무료화와 AI 유료화: Canva는 Affinity를 무료로 풀고 AI 기능만 유료로 제공한다.", subbul, "-"))
S.append(B("<b>문제의식</b>: 이용자의 법적 권리는 줄고 기술적 복제 능력은 늘어나는 상반된 흐름 속에서, "
           "플랫폼의 권력이 약해지는지, 형태를 바꿔 유지되는지, 다른 행위자에게 넘어가는지는 아직 분명하지 않다."))

S.append(Paragraph("2. 연구 목적", h))
S.append(Paragraph(
    "본 연구는 AI 기반 복제·대체가 미디어 소프트웨어, 즉 미디어 소비 쪽의 게임과 생산 쪽의 창작 도구에서 "
    "권력 구조를 어떻게 바꾸는지 밝히는 것을 목적으로 한다. 구체적인 목표는 다음과 같다.", body))
for n, t in [
    ("(1)", "미디어 소프트웨어를 코드·기능, 실행 환경, 인터페이스, 데이터, 서비스, 네트워크, 계약·법, 규칙 설정의 "
            "여덟 층위로 나누고, 각 층위를 어느 행위자가 통제하게 되었는지 서술한다."),
    ("(2)", "권력이 사용자와 공동체에게 분산된다는 <b>침식</b>, 플랫폼이 복제할 수 없는 층위로 통제를 옮긴다는 "
            "<b>이동</b>, 의존이 AI 제공자에게 넘어간다는 <b>이전</b>의 세 가지 기대 가운데 무엇이 영역과 행위자에 따라 "
            "더 잘 들어맞는지 판단한다."),
    ("(3)", "게임 플랫폼과 창작 소프트웨어 플랫폼이 복제·대체 압력에 어떻게 다르게 대응하는지 비교한다."),
    ("(4)", "'복제·대체' 개념, 미디어 소프트웨어의 층위 모형, 이용자의 법적 권리와 사실상 능력 사이의 괴리를 "
            "미디어 연구의 개념으로 제시한다."),
]:
    S.append(Paragraph(f"{n}&nbsp;&nbsp;{t}", item))

S.append(Paragraph("3. 연구 질문", h))
S.append(Paragraph(
    "AI가 미디어 소프트웨어(게임과 창작 도구)를 복제하고 대체하는 데 드는 비용과 숙련 장벽을 낮추면서, "
    "플랫폼 보유자, 권리자, 사용자, 창작·역공학 공동체, AI 제공자 사이의 권력 구조는 어떻게 변하는가? "
    "그 변화는 영역과 행위자에 따라 어떻게 다른가?", rq))


doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=18*mm, bottomMargin=16*mm, title="연구 개요 초안", author="김권택")
doc.build(S)
