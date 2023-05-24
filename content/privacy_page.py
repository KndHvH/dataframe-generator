import streamlit as st

def privacy_page():
    with st.expander("", expanded=True):
        
        st.markdown(
        """
        # Política de Privacidade

        Esta Política de Privacidade tem como objetivo informar sobre as práticas de geração, uso e divulgação de dados pessoais pela ferramenta de geração de dados fictícios desenvolvida por Matias Cornelsen Herklotz (doravante denominada "Dataframe Generator").

        ### 1. Geração e Uso de Dados Pessoais

        A ferramenta é projetada para gerar dados fictícios para testes em processos de ETL, incluindo informações como CPFs, nomes, endereços, entre outros. Esses dados são gerados de forma aleatória e não são associados a nenhuma pessoa real.

        Ao utilizar a ferramenta, você concorda que os dados pessoais gerados serão coletados e armazenados temporariamente com a finalidade exclusiva de facilitar os testes em processos de ETL. Esses dados não serão utilizados para qualquer outra finalidade além daquelas relacionadas aos testes de ETL.

        ### 2. Proteção de Dados Pessoais

        A segurança e a privacidade dos dados pessoais gerados são de extrema importância para nós. Comprometemo-nos a não compartilhar, vender ou transferir de qualquer forma os dados pessoais gerados pela ferramenta para terceiros, a menos que seja exigido por lei.

        ### 3. Retenção de Dados Pessoais

        Os dados pessoais gerados pela ferramenta serão retidos apenas pelo tempo necessário para a realização dos testes de ETL. Após esse período, os dados deverão ser devidamente excluídos.

        ### 4. Responsabilidade

        Matias Cornelsen Herklotz atua como responsável pelo desenvolvimento e manutenção da ferramenta, garantindo que os dados gerados sejam fictícios e exclusivos para uso em testes de ETL. Em caso de dúvidas, preocupações ou solicitações relacionadas à privacidade dos dados gerados, você pode entrar em contato através do seguinte e-mail: matias.herklotz@globalhitss.com.br.

        ### 5. Uso Responsável

        Ao utilizar a ferramenta, você concorda em utilizar os dados gerados exclusivamente para fins de teste em processos de ETL. Você reconhece que é sua responsabilidade garantir o uso adequado e legal dos dados fictícios gerados e se compromete a não utilizar esses dados para fins ilegais, prejudiciais ou não autorizados.

        ### 6. Alterações nesta Política de Privacidade

        Reservamo-nos o direito de atualizar esta Política de Privacidade periodicamente. Recomendamos que você reveja esta política regularmente para se manter informado sobre nossas práticas de privacidade.

        Esta Política de Privacidade foi atualizada pela última vez em 24/05/2023.

        Ao utilizar a ferramenta, você concorda com os termos desta Política de Privacidade. Se você não concordar com estes termos, não utilize a ferramenta.

        """)

        st.text('')
        if st.button('Concordo',use_container_width=True):
            st.session_state.lgpd = True
            st.experimental_rerun()

        